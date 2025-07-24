#!/usr/bin/env python3
"""
Script para automatizar la subida de un proyecto local a GitHub.
Automatiza el proceso completo desde la inicialización de Git hasta el push al repositorio remoto.
"""

import os
import subprocess
import requests
import getpass
import sys
import json


def check_git_installation():
    """Verifica que Git esté instalado en el sistema."""
    try:
        result = subprocess.run(
            ["git", "--version"], 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"✓ Git está instalado: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: Git no está instalado o no se encuentra en el PATH del sistema.")
        print("Por favor, instala Git desde: https://git-scm.com/downloads")
        return False


def get_user_input():
    """Solicita al usuario toda la información necesaria."""
    print("\n" + "="*60)
    print("CONFIGURACIÓN DEL REPOSITORIO GITHUB")
    print("="*60)
    
    # Token de acceso personal (entrada oculta)
    token = getpass.getpass("🔑 Ingresa tu Token de Acceso Personal de GitHub: ").strip()
    if not token:
        print("❌ Error: El token es obligatorio.")
        sys.exit(1)
    
    # Nombre del repositorio
    repo_name = input("📁 Nombre del repositorio: ").strip()
    if not repo_name:
        print("❌ Error: El nombre del repositorio es obligatorio.")
        sys.exit(1)
    
    # Descripción opcional
    description = input("📝 Descripción (opcional): ").strip()
    
    # Visibilidad del repositorio
    while True:
        visibility = input("🔒 Visibilidad (publico/privado) [publico]: ").strip().lower()
        if not visibility:
            visibility = "publico"
        if visibility in ['publico', 'público', 'public']:
            visibility = "publico"
            break
        elif visibility in ['privado', 'private']:
            visibility = "privado"
            break
        else:
            print("❌ Opción inválida. Ingresa 'publico' o 'privado'.")
    
    # Ruta del proyecto local
    default_path = os.getcwd()
    project_path = input(f"📂 Ruta del proyecto local [{default_path}]: ").strip()
    if not project_path:
        project_path = default_path
    
    # Validar que la ruta existe
    if not os.path.isdir(project_path):
        print(f"❌ Error: La ruta especificada no existe: {project_path}")
        sys.exit(1)
    
    return {
        'token': token,
        'repo_name': repo_name,
        'description': description,
        'visibility': visibility,
        'project_path': project_path
    }


def initialize_git_repo(project_path):
    """Inicializa el repositorio Git si no existe."""
    os.chdir(project_path)
    
    if not os.path.isdir(".git"):
        print("🔧 No se encontró repositorio Git. Inicializando nuevo repositorio...")
        try:
            subprocess.run(["git", "init"], check=True, capture_output=True)
            print("✓ Repositorio Git inicializado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al inicializar Git: {e}")
            sys.exit(1)
    else:
        print("✓ Repositorio Git ya existe.")


def stage_and_commit():
    """Añade todos los archivos y hace el commit inicial."""
    try:
        print("📦 Añadiendo archivos al repositorio...")
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        
        # Verificar si hay cambios para commitear
        result = subprocess.run(
            ["git", "status", "--porcelain"], 
            check=True, 
            capture_output=True, 
            text=True
        )
        
        if not result.stdout.strip():
            print("ℹ️  No hay cambios para commitear.")
            return False
        
        print("💾 Creando commit inicial...")
        subprocess.run(
            ["git", "commit", "-m", "Initial commit - Subido automáticamente"], 
            check=True, 
            capture_output=True
        )
        print("✓ Commit inicial creado correctamente.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante git add/commit: {e}")
        sys.exit(1)


def get_current_branch():
    """Determina la rama actual (main/master)."""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"], 
            check=True, 
            capture_output=True, 
            text=True
        )
        branch = result.stdout.strip()
        
        if not branch:
            # Si no hay rama actual, crear main
            subprocess.run(["git", "checkout", "-b", "main"], check=True, capture_output=True)
            branch = "main"
            
    except subprocess.CalledProcessError:
        # Fallback a main si hay algún error
        try:
            subprocess.run(["git", "checkout", "-b", "main"], check=True, capture_output=True)
            branch = "main"
        except subprocess.CalledProcessError:
            branch = "main"
    
    print(f"🌿 Usando rama: {branch}")
    return branch


def create_github_repo(token, repo_name, description, visibility):
    """Crea el repositorio remoto en GitHub usando la API."""
    api_url = "https://api.github.com/user/repos"
    
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "name": repo_name,
        "description": description if description else f"Repositorio {repo_name}",
        "private": True if visibility == "privado" else False
    }
    
    print("🚀 Creando repositorio remoto en GitHub...")
    
    try:
        response = requests.post(api_url, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 201:
            repo_data = response.json()
            print(f"✓ Repositorio creado exitosamente: {repo_data['html_url']}")
            return repo_data['clone_url']
            
        elif response.status_code == 422:
            error_data = response.json()
            if "name already exists" in str(error_data):
                print(f"⚠️  El repositorio '{repo_name}' ya existe en tu cuenta de GitHub.")
                # Intentar obtener la URL del repositorio existente
                try:
                    get_url = f"https://api.github.com/repos/{get_github_username(token)}/{repo_name}"
                    get_response = requests.get(get_url, headers=headers, timeout=30)
                    if get_response.status_code == 200:
                        existing_repo = get_response.json()
                        return existing_repo['clone_url']
                except:
                    pass
                return f"https://github.com/{get_github_username(token)}/{repo_name}.git"
            else:
                print(f"❌ Error de validación: {error_data}")
                sys.exit(1)
                
        elif response.status_code == 401:
            print("❌ Error de autenticación: Token inválido o sin permisos.")
            print("Verifica que tu token tenga los permisos 'repo' habilitados.")
            sys.exit(1)
            
        else:
            print(f"❌ Error al crear repositorio (Código {response.status_code}):")
            try:
                error_info = response.json()
                print(json.dumps(error_info, indent=2))
            except:
                print(response.text)
            sys.exit(1)
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión con GitHub: {e}")
        sys.exit(1)


def get_github_username(token):
    """Obtiene el nombre de usuario de GitHub usando el token."""
    try:
        headers = {"Authorization": f"token {token}"}
        response = requests.get("https://api.github.com/user", headers=headers, timeout=30)
        if response.status_code == 200:
            return response.json()['login']
    except:
        pass
    return "usuario"


def add_remote_and_push(clone_url, branch):
    """Añade el remote origin y hace push del commit."""
    try:
        # Verificar si ya existe un remote origin
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"], 
            capture_output=True, 
            text=True
        )
        
        if result.returncode == 0:
            print("🔗 Remote origin ya existe. Actualizando URL...")
            subprocess.run(["git", "remote", "set-url", "origin", clone_url], check=True)
        else:
            print("🔗 Añadiendo remote origin...")
            subprocess.run(["git", "remote", "add", "origin", clone_url], check=True)
        
        print("📤 Subiendo código a GitHub...")
        subprocess.run(["git", "push", "-u", "origin", branch], check=True)
        print("✓ Código subido exitosamente a GitHub!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante la configuración del remote o push: {e}")
        print("Verifica que tengas permisos de escritura en el repositorio.")
        sys.exit(1)


def main():
    """Función principal que ejecuta todo el proceso."""
    print("🚀 AUTOMATIZACIÓN DE SUBIDA A GITHUB")
    print("="*60)
    
    # 1. Verificar instalación de Git
    if not check_git_installation():
        sys.exit(1)
    
    # 2. Obtener información del usuario
    config = get_user_input()
    
    # 3. Cambiar al directorio del proyecto
    original_dir = os.getcwd()
    
    try:
        # 4. Inicializar repositorio Git
        initialize_git_repo(config['project_path'])
        
        # 5. Añadir archivos y hacer commit
        has_changes = stage_and_commit()
        
        # 6. Determinar rama actual
        branch = get_current_branch()
        
        # 7. Crear repositorio remoto en GitHub
        clone_url = create_github_repo(
            config['token'], 
            config['repo_name'], 
            config['description'], 
            config['visibility']
        )
        
        # 8. Añadir remote y hacer push
        add_remote_and_push(clone_url, branch)
        
        # 9. Mensaje de éxito
        print("\n" + "="*60)
        print("🎉 ¡PROCESO COMPLETADO EXITOSAMENTE!")
        print("="*60)
        print(f"📁 Repositorio: {config['repo_name']}")
        print(f"🔒 Visibilidad: {config['visibility']}")
        print(f"🌿 Rama: {branch}")
        print(f"🌐 URL: https://github.com/{get_github_username(config['token'])}/{config['repo_name']}")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n❌ Proceso cancelado por el usuario.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
    finally:
        # Volver al directorio original
        os.chdir(original_dir)


if __name__ == "__main__":
    main()
