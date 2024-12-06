# Gestor de Usuarios y Contraseñas

Este es un proyecto desarrollado en Python que permite gestionar usuarios y contraseñas de forma segura utilizando cifrado con la biblioteca `cryptography.fernet`. El programa ofrece funcionalidades para ingresar nuevas contraseñas, cambiar contraseñas existentes y visualizar contraseñas almacenadas, todo bajo el resguardo de una clave maestra.

## Características
- **Ingreso de usuario y contraseña:** Genera una contraseña segura para un usuario, con opciones para personalizar longitud, uso de mayúsculas, números y símbolos.
- **Cambio de contraseña:** Valida la contraseña anterior antes de permitir el cambio. La nueva contraseña puede personalizarse de la misma manera que al generarla.
- **Visualización de contraseñas:** Muestra las contraseñas almacenadas solo si se ingresa la clave maestra correcta. Permite buscar por usuario específico o mostrar todas las contraseñas.
- **Cifrado seguro:** Utiliza la biblioteca `cryptography.fernet` para garantizar que las contraseñas estén protegidas en el almacenamiento.

## Requisitos
- Python 3.6 o superior.
- Biblioteca `cryptography`.

## Uso
- **Opciones disponibles en el menú principal:**
   - **1. Ingresar usuario y contraseña:**
     Solicita el nombre del usuario.
     Permite generar una contraseña personalizada según las preferencias del usuario.
     Guarda el usuario y la contraseña cifrada en un archivo local.

   - **2. Cambiar contraseña:**
     Valida la contraseña actual antes de permitir el cambio.
     Solicita opciones para la generación de la nueva contraseña.

   - **3. Visualizar contraseñas:**
     Solicita la clave maestra antes de mostrar las contraseñas almacenadas.
     Permite buscar la contraseña de un usuario específico o mostrar todas las contraseñas.

   - **4. Salir:**
     Finaliza la ejecución del programa.

## Estructura del Proyecto
- `usuarios_contraseñas.txt`: Archivo donde se almacenan las contraseñas cifradas junto con los nombres de usuario.
- `main.py`: Código principal del programa.

## Posibles Mejoras
- **Gestión de usuarios:**
   Implementar un sistema de autenticación para identificar al usuario antes de realizar operaciones (como cambio o visualización de contraseñas).

- **Límites de intentos:**
   Restringir la cantidad de intentos fallidos al ingresar la clave maestra o la contraseña actual.

- **Interfaz gráfica:**
   Integrar una interfaz gráfica de usuario (GUI) utilizando bibliotecas como `tkinter` o `PyQt`.

- **Seguridad avanzada:**
   Reforzar la seguridad utilizando hashing para almacenar contraseñas (en lugar de cifrarlas directamente).

- **Reportes de actividad:**
   Añadir un registro de actividad para rastrear cambios en las contraseñas.
