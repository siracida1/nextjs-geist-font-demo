# 📖 Ejemplo de Uso del Script upload_to_github.py

## 🚀 Ejecución Paso a Paso

### 1. Preparación
Antes de ejecutar el script, asegúrate de tener:
- ✅ Python 3.6+ instalado
- ✅ Git instalado
- ✅ Token de GitHub creado
- ✅ Módulo `requests` instalado (`pip install requests`)

### 2. Ejecución del Script
```bash
python3 upload_to_github.py
```

### 3. Ejemplo de Sesión Interactiva

```
🚀 AUTOMATIZACIÓN DE SUBIDA A GITHUB
============================================================
✓ Git está instalado: git version 2.30.2

============================================================
CONFIGURACIÓN DEL REPOSITORIO GITHUB
============================================================
🔑 Ingresa tu Token de Acceso Personal de GitHub: [entrada oculta]
📁 Nombre del repositorio: mi-app-react
📝 Descripción (opcional): Aplicación React con componentes modernos
🔒 Visibilidad (publico/privado) [publico]: publico
📂 Ruta del proyecto local [/project/sandbox/user-workspace]: 

🔧 No se encontró repositorio Git. Inicializando nuevo repositorio...
✓ Repositorio Git inicializado correctamente.
📦 Añadiendo archivos al repositorio...
💾 Creando commit inicial...
✓ Commit inicial creado correctamente.
🌿 Usando rama: main
🚀 Creando repositorio remoto en GitHub...
✓ Repositorio creado exitosamente: https://github.com/usuario/mi-app-react
🔗 Añadiendo remote origin...
📤 Subiendo código a GitHub...
✓ Código subido exitosamente a GitHub!

============================================================
🎉 ¡PROCESO COMPLETADO EXITOSAMENTE!
============================================================
📁 Repositorio: mi-app-react
🔒 Visibilidad: publico
🌿 Rama: main
🌐 URL: https://github.com/usuario/mi-app-react
============================================================
```

## 🔧 Casos de Uso Comunes

### Caso 1: Proyecto Nuevo (Sin Git)
- El script detecta que no hay `.git/`
- Inicializa automáticamente el repositorio
- Añade todos los archivos y hace commit
- Crea el repositorio en GitHub
- Configura remote y hace push

### Caso 2: Proyecto Existente (Con Git)
- El script detecta repositorio Git existente
- Añade archivos nuevos/modificados
- Hace commit de cambios
- Crea repositorio remoto
- Configura remote y hace push

### Caso 3: Repositorio Ya Existe en GitHub
- El script detecta que el repositorio ya existe
- Obtiene la URL del repositorio existente
- Configura remote con la URL existente
- Hace push de los cambios locales

## 🛠️ Personalización de Respuestas

### Respuestas Típicas:

**Token de GitHub:**
```
🔑 Ingresa tu Token de Acceso Personal de GitHub: [se oculta mientras escribes]
```

**Nombre del repositorio:**
```
📁 Nombre del repositorio: mi-proyecto-web
```

**Descripción (opcional):**
```
📝 Descripción (opcional): [Enter para omitir]
o
📝 Descripción (opcional): Mi aplicación web con Next.js
```

**Visibilidad:**
```
🔒 Visibilidad (publico/privado) [publico]: [Enter para público]
o
🔒 Visibilidad (publico/privado) [publico]: privado
```

**Ruta del proyecto:**
```
📂 Ruta del proyecto local [/ruta/actual]: [Enter para directorio actual]
o
📂 Ruta del proyecto local [/ruta/actual]: /home/usuario/mi-proyecto
```

## 🚨 Manejo de Errores Comunes

### Error: Token Inválido
```
❌ Error de autenticación: Token inválido o sin permisos.
Verifica que tu token tenga los permisos 'repo' habilitados.
```
**Solución:** Verifica tu token en GitHub Settings → Developer settings

### Error: Repositorio Ya Existe
```
⚠️ El repositorio 'mi-proyecto' ya existe en tu cuenta de GitHub.
```
**Comportamiento:** El script continúa y usa el repositorio existente

### Error: Git No Instalado
```
❌ Error: Git no está instalado o no se encuentra en el PATH del sistema.
Por favor, instala Git desde: https://git-scm.com/downloads
```
**Solución:** Instalar Git desde el sitio oficial

## 📋 Checklist Pre-Ejecución

Antes de ejecutar el script, verifica:

- [ ] Python 3.6+ instalado (`python3 --version`)
- [ ] Git instalado (`git --version`)
- [ ] Módulo requests instalado (`pip install requests`)
- [ ] Token de GitHub creado con permisos 'repo'
- [ ] Estás en el directorio correcto del proyecto
- [ ] Tienes conexión a Internet

## 🎯 Resultados Esperados

Después de una ejecución exitosa:

1. **Repositorio Local:**
   - Inicializado con Git (si no existía)
   - Todos los archivos añadidos y commiteados
   - Remote 'origin' configurado

2. **Repositorio GitHub:**
   - Creado con el nombre especificado
   - Visibilidad configurada (público/privado)
   - Código subido en la rama principal

3. **Archivos Locales:**
   - `.git/` directorio creado
   - `.git/config` con remote origin
   - Historial de commits iniciado

## 🔄 Uso Repetido

Para proyectos que ya han sido subidos:
- El script detectará el repositorio existente
- Solo hará commit de cambios nuevos
- Actualizará el repositorio remoto con push

## 💡 Consejos Adicionales

1. **Backup:** Siempre haz backup antes de ejecutar en proyectos importantes
2. **Gitignore:** Crea un `.gitignore` antes de ejecutar para excluir archivos innecesarios
3. **Branches:** El script usa la rama actual o crea 'main' por defecto
4. **Tokens:** Guarda tu token de forma segura, no lo compartas

---

¡Listo para automatizar tus subidas a GitHub! 🚀
