# Escape Room: La Arena del Gladiador

# Nombre del jugador
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")

# Bucle principal
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    # Validación
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    # Opción 1: Ataque Pesado
    if opcion == "1":
        if vida_enemigo < 20:
            danio = danio_base * 1.5
            print("¡Golpe crítico!")
        else:
            danio = danio_base

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    # Opción 2: Ráfaga Veloz
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Opción 3: Curar
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones!")

    # Turno del enemigo (si sigue vivo)
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

# Resultado final
print("\n--- FIN DEL COMBATE ---")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")