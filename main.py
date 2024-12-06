from cryptography.fernet import Fernet
import hashlib
import base64
import random
import string

# Derivar una clave fija desde la clave maestra
def convertir_clave(clave_maestra):
    return base64.urlsafe_b64encode(hashlib.sha256(clave_maestra.encode()).digest()[:32])

# Validar entradas del usuario
def input_validado(prompt, tipo=str):
    while True:
        entrada = input(prompt).strip()
        if entrada:  # Validar que no sea vacío
            try:
                return tipo(entrada)  # Convertir al tipo esperado
            except ValueError:
                print(f"Por favor, introduce un valor válido ({tipo.__name__}).")
        else:
            print("Este campo no puede estar vacío. Inténtalo de nuevo.")

# Generar una contraseña segura con opciones personalizadas
def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase  # Minúsculas por defecto
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Guardar usuario y contraseña encriptada
def guardar_usuario_contraseña(usuario, contraseña, fernet):
    with open("usuarios_contraseñas.txt", "ab") as archivo:
        data = f"{usuario}:{fernet.encrypt(contraseña.encode()).decode()}\n"
        archivo.write(data.encode())
    print("¡Usuario y contraseña guardados encriptados!")

# Validar cambio de contraseña
def cambiar_contraseña(usuario, fernet):
    try:
        with open("usuarios_contraseñas.txt", "r") as archivo:
            lineas = archivo.readlines()

        encontrado = False
        for i, linea in enumerate(lineas):
            user, enc_password = linea.strip().split(":", 1)
            if user == usuario:
                encontrado = True
                old_password = input_validado("Introduce tu contraseña actual: ")
                if fernet.decrypt(enc_password.encode()).decode() == old_password:
                    print("Generando nueva contraseña...")
                    longitud = input_validado("¿Longitud de la nueva contraseña? (mínimo 8): ", int)
                    if longitud < 8:
                        print("La longitud debe ser al menos 8.")
                        return

                    incluir_mayusculas = input_validado("¿Incluir mayúsculas? (s/n): ").lower() == 's'
                    incluir_numeros = input_validado("¿Incluir números? (s/n): ").lower() == 's'
                    incluir_simbolos = input_validado("¿Incluir símbolos? (s/n): ").lower() == 's'

                    nueva_contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
                    print(f"Nueva contraseña generada: {nueva_contraseña}")
                    lineas[i] = f"{usuario}:{fernet.encrypt(nueva_contraseña.encode()).decode()}\n"
                    with open("usuarios_contraseñas.txt", "w") as archivo:
                        archivo.writelines(lineas)
                    print("¡Contraseña actualizada exitosamente!")
                    return
                else:
                    print("Contraseña actual incorrecta.")
                    return

        if not encontrado:
            print("Usuario no encontrado.")
    except FileNotFoundError:
        print("No hay usuarios registrados aún.")

# Mostrar contraseñas desencriptadas
def mostrar_contraseñas(fernet):
    clave_maestra = input_validado("Introduce la clave maestra: ")
    if clave_maestra != "Masterkey.123":
        print("Clave maestra incorrecta. Acceso denegado.")
        return

    try:
        with open("usuarios_contraseñas.txt", "r") as archivo:
            lineas = archivo.readlines()
            opcion = input_validado("¿Deseas buscar por usuario? (s/n): ").lower()
            if opcion == "s":
                usuario = input_validado("Introduce el nombre del usuario: ")
                for linea in lineas:
                    user, enc_password = linea.strip().split(":", 1)
                    if user == usuario:
                        print(f"{user}: {fernet.decrypt(enc_password.encode()).decode()}")
                        return
                print("Usuario no encontrado.")
            else:
                print("\nUsuarios y contraseñas desencriptadas:")
                for linea in lineas:
                    user, enc_password = linea.strip().split(":", 1)
                    print(f"{user}: {fernet.decrypt(enc_password.encode()).decode()}")

    except FileNotFoundError:
        print("No hay usuarios registrados aún.")
    except Exception as e:
        print(f"Error al desencriptar: {e}")

# Función principal
def main():
    # Clave fija para cifrar contraseñas
    clave_fija = convertir_clave("Masterkey.123")
    fernet = Fernet(clave_fija)

    while True:
        print("\nOpciones:")
        print("1. Ingresar usuario y contraseña")
        print("2. Cambiar contraseña")
        print("3. Visualizar contraseñas")
        print("4. Salir")
        opcion = input_validado("Elige una opción: ")

        if opcion == "1":
            usuario = input_validado("Introduce el nombre de usuario: ")
            longitud = input_validado("¿Longitud de la contraseña? (mínimo 8): ", int)
            if longitud < 8:
                print("La longitud debe ser al menos 8.")
                continue

            incluir_mayusculas = input_validado("¿Incluir mayúsculas? (s/n): ").lower() == 's'
            incluir_numeros = input_validado("¿Incluir números? (s/n): ").lower() == 's'
            incluir_simbolos = input_validado("¿Incluir símbolos? (s/n): ").lower() == 's'

            contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
            print(f"Contraseña generada para {usuario}: {contraseña}")
            if input_validado("¿Deseas guardarla? (s/n): ").lower() == "s":
                guardar_usuario_contraseña(usuario, contraseña, fernet)

        elif opcion == "2":
            usuario = input_validado("Introduce el nombre de usuario: ")
            cambiar_contraseña(usuario, fernet)

        elif opcion == "3":
            mostrar_contraseñas(fernet)

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
