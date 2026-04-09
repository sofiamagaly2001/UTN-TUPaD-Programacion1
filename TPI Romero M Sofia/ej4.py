# Escape Room: La bóveda

# Variables
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# Nombre
nombre = input("Nombre del agente: ")

# Validación del nombre
while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Nombre del agente: ")

# Empieza el juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")
    print("\n--MENU DE ACCIONES--")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione opción: ")

    # Validación
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: ingrese un número válido.")
        opcion = input("Seleccione nuevamente: ")

    # Opción 1: Forzar cerradura
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # Regla anti-spam
        if racha_forzar == 3:
            alarma = True
            print("¡Forzaste demasiado! La cerradura se trabó y se activó la alarma.")

        else:
            if energia < 40:
                numero = input("Elegir un número del 1 al 3: ")
                while not numero.isdigit() or numero not in ["1", "2", "3"]:
                    print("Error: ingrese un número válido.")
                    numero = input("Elegir un número del 1 al 3: ")

                if numero == "3":
                    alarma = True

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura abierta.")

    # Opción 2: Hackear panel
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Cerradura abierta.")

    # Opción 3: Descansar
    elif opcion == "3":
        energia += 15
        tiempo -= 1
        racha_forzar = 0

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

        print("Descansaste.")

    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma.")
        break

# Resultado final
print("\n--- RESULTADO FINAL ---")

if cerraduras_abiertas == 3:
    print("¡Misión cumplida!")
elif alarma:
    print("Fracaso: se activó la alarma.")
elif energia <= 0:
    print("Fracaso: sin energía.")
elif tiempo <= 0:
    print("Fracaso: sin tiempo.")