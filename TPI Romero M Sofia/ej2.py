# Acceso al Campus y Menú Seguro
# Variables
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

# Login
while intentos < 3 and not acceso:
    print(f"Intento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
    else:
        intentos += 1
        print("Error: credenciales inválidas.")

# Bloqueo
if not acceso:
    print("Cuenta bloqueada")

# Menú
if acceso:
    opcion = ""
    while opcion != "4":
        print("\n-- MENÚ --")
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit() or opcion not in ["1", "2", "3", "4"]:
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")
        if opcion == "1":
            print("Estado: Inscripto")

        elif opcion == "2":
            nueva_clave = input("Ingresar nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Ingresar nueva clave: ")

            confirmacion = input("Confirme su nueva clave: ")

            while nueva_clave != confirmacion:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirme su nueva clave: ")

            clave_correcta = nueva_clave
            print("Clave cambiada con éxito.")

        elif opcion == "3":
            print("El éxito es la suma de pequeños esfuerzos repetidos día tras día.")

        elif opcion == "4":
            print("Saliendo del sistema...")
