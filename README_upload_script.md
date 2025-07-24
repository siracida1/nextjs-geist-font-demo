# 🚀 Script de Automatización para Subir Proyectos a GitHub

Este script de Python automatiza completamente el proceso de subir un proyecto local a GitHub, desde la inicialización de Git hasta el push al repositorio remoto.

## ✨ Características

- ✅ **Verificación automática** de instalación de Git
- 🔐 **Entrada segura** del token de GitHub (sin mostrar en pantalla)
- 📁 **Inicialización automática** de repositorio Git si no existe
- 📦 **Commit automático** de todos los archivos
- 🌐 **Creación automática** del repositorio remoto en GitHub
- 🌿 **Detección inteligente** de rama principal (main/master)
- 🔄 **Push automático** al repositorio remoto
- 🛡️ **Manejo robusto de errores** en cada paso
- 📊 **Mensajes de progreso** claros y detallados

## 📋 Requisitos

### Software Necesario
- **Python 3.6+** instalado en el sistema
- **Git** instalado y disponible en PATH
- **Conexión a Internet** para acceder a la API de GitHub

### Módulos de Python
El script utiliza los siguientes módulos (todos incluidos en Python estándar excepto `requests`):
- `os` - Operaciones del sistema de archivos
- `subprocess` - Ejecución de comandos Git
- `requests` - Llamadas a la API de GitHub
- `getpass` - Entrada segura del token
- `sys` - Control del flujo del programa
- `json` - Manejo de respuestas JSON

### Instalación de Dependencias
```bash
pip install requests
```

## 🔑 Configuración del Token de GitHub

### Paso 1: Crear un Personal Access Token
1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Haz clic en "Generate new token (classic)"
3. Selecciona los siguientes permisos:
   - ✅ `repo` (acceso completo a repositorios)
   - ✅ `user` (acceso a información del usuario)
4. Copia el token generado (¡guárdalo de forma segura!)

### Paso 2: Permisos Necesarios
El token debe tener al menos estos scopes:
- `repo` - Para crear y modificar repositorios
- `user` - Para obtener información del usuario

## 🚀 Uso del Script

### Ejecución Básica
```bash
python3 upload_to_github.py
```

### Proceso Interactivo
El script te solicitará la siguiente información:

1. **🔑 Token de GitHub**: Tu Personal Access Token (entrada oculta)
2. **📁 Nombre del repositorio**: Nombre para el nuevo repositorio
3. **📝 Descripción**: Descripción opcional del repositorio
4. **🔒 Visibilidad**: `publico` o `privado`
5. **📂 Ruta del proyecto**: Ruta local del proyecto (por defecto: directorio actual)

### Ejemplo de Ejecución
```
🚀 AUTOMATIZACIÓN DE SUBIDA A GITHUB
============================================================
✓ Git está instalado: git version 2.30.2

============================================================
CONFIGURACIÓN DEL REPOSITORIO GITHUB
============================================================
🔑 Ingresa tu Token de Acceso Personal de GitHub: [oculto]
📁 Nombre del repositorio: mi-proyecto-web
📝 Descripción (opcional): Mi aplicación web con React
🔒 Visibilidad (publico/privado) [publico]: publico
📂 Ruta del proyecto local [/ruta/actual]: 

🔧 No se encontró repositorio Git. Inicializando nuevo repositorio...
✓ Repositorio Git inicializado correctamente.
📦 Añadiendo archivos al repositorio...
💾 Creando commit inicial...
✓ Commit inicial creado correctamente.
🌿 Usando rama: main
🚀 Creando repositorio remoto en GitHub...
✓ Repositorio creado exitosamente: https://github.com/usuario/mi-proyecto-web
🔗 Añadiendo remote origin...
📤 Subiendo código a GitHub...
✓ Código subido exitosamente a GitHub!

============================================================
🎉 ¡PROCESO COMPLETADO EXITOSAMENTE!
============================================================
📁 Repositorio: mi-proyecto-web
🔒 Visibilidad: publico
🌿 Rama: main
🌐 URL: https://github.com/usuario/mi-proyecto-web
============================================================
```

## 🛠️ Funcionalidades Detalladas

### 1. Verificación de Git
- Comprueba que Git esté instalado y accesible
- Muestra la versión de Git instalada
- Termina el script si Git no está disponible

### 2. Validación de Entrada
- Valida que el token no esté vacío
- Verifica que el nombre del repositorio sea válido
- Comprueba que la ruta del proyecto exista
- Normaliza la opción de visibilidad

### 3. Inicialización de Git
- Detecta si ya existe un repositorio Git
- Inicializa un nuevo repositorio si es necesario
- Cambia al directorio del proyecto especificado

### 4. Gestión de Commits
- Añade todos los archivos al staging area
- Verifica si hay cambios para commitear
- Crea un commit inicial con mensaje descriptivo

### 5. Detección de Rama
- Detecta la rama actual automáticamente
- Crea la rama 'main' si no existe ninguna
- Maneja casos especiales de repositorios nuevos

### 6. Creación de Repositorio Remoto
- Utiliza la API REST de GitHub v3
- Maneja repositorios públicos y privados
- Gestiona casos de repositorios existentes
- Proporciona URLs de acceso directo

### 7. Configuración de Remote y Push
- Configura el remote origin automáticamente
- Actualiza remote existente si es necesario
- Realiza push con tracking de rama upstream

## 🚨 Manejo de Errores

### Errores Comunes y Soluciones

#### Error de Autenticación (401)
```
❌ Error de autenticación: Token inválido o sin permisos.
```
**Solución**: Verifica que tu token tenga los permisos 'repo' habilitados.

#### Repositorio Ya Existe (422)
```
⚠️ El repositorio 'nombre' ya existe en tu cuenta de GitHub.
```
**Comportamiento**: El script detecta el repositorio existente y continúa con el push.

#### Git No Instalado
```
❌ Error: Git no está instalado o no se encuentra en el PATH del sistema.
```
**Solución**: Instala Git desde https://git-scm.com/downloads

#### Error de Conexión
```
❌ Error de conexión con GitHub: [detalles del error]
```
**Solución**: Verifica tu conexión a Internet y el estado de GitHub.

## 🔧 Personalización

### Modificar Mensaje de Commit
Edita la línea 108 en el script:
```python
subprocess.run(
    ["git", "commit", "-m", "Tu mensaje personalizado"], 
    check=True, 
    capture_output=True
)
```

### Cambiar Rama por Defecto
Modifica la función `get_current_branch()` para usar una rama diferente:
```python
branch = "develop"  # En lugar de "main"
```

### Añadir Archivos Específicos
Reemplaza `git add .` con archivos específicos:
```python
subprocess.run(["git", "add", "archivo1.py", "archivo2.js"], check=True)
```

## 📁 Estructura del Proyecto

```
proyecto/
├── upload_to_github.py     # Script principal
├── README_upload_script.md # Esta documentación
└── tu-proyecto/           # Tu código fuente
    ├── archivo1.py
    ├── archivo2.js
    └── ...
```

## 🔒 Seguridad

### Mejores Prácticas
- ✅ **Nunca hardcodees** el token en el script
- ✅ **Usa entrada oculta** para el token (getpass)
- ✅ **Revoca tokens** no utilizados regularmente
- ✅ **Usa tokens con permisos mínimos** necesarios
- ✅ **No compartas** tokens en repositorios públicos

### Almacenamiento Seguro del Token
Considera usar variables de entorno para uso frecuente:
```bash
export GITHUB_TOKEN="tu_token_aqui"
```

## 🐛 Solución de Problemas

### Debug Mode
Para obtener más información sobre errores, modifica el script temporalmente:
```python
# Añadir al inicio de main()
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Verificar Estado de Git
```bash
git status
git remote -v
git log --oneline
```

### Limpiar Configuración
Si necesitas empezar de nuevo:
```bash
rm -rf .git
git init
```

## 📞 Soporte

### Recursos Útiles
- [Documentación de Git](https://git-scm.com/doc)
- [API de GitHub](https://docs.github.com/en/rest)
- [Tokens de GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

### Problemas Conocidos
- El script requiere Python 3.6+ para f-strings
- Algunos firewalls corporativos pueden bloquear la API de GitHub
- Windows puede requerir `python` en lugar de `python3`

## 📄 Licencia

Este script es de uso libre. Puedes modificarlo y distribuirlo según tus necesidades.

---

**¡Disfruta automatizando tus subidas a GitHub! 🚀**
