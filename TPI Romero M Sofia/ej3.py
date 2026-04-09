# Agenda de Turnos
# Nombre
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ") 

# Variables vacías
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

# Menú
while opcion != "5":
    print("\n--AGENDA DE TURNOS--")
    print("1) Reservar 2) Cancelar 3) Ver Día 4) Resumen 5) Salir")
    opcion = input("Seleccione opción: ")
    # Validación
    while not opcion.isdigit() or opcion not in ["1", "2", "3", "4", "5"]:
        print("Error: ingrese un número válido.")
        opcion = input("Seleccione opción: ")
    # Opción: Reservar turno
    if opcion == "1":
        dia = input("Elija día (1=Lunes, 2=Martes): ")
        # Validación del día
        while dia != "1" and dia != "2":
            dia = input("Error. Elija día (1=Lunes, 2=Martes): ")
        # Nombre y validación del paciente
        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error. Nombre del paciente: ")
        # Día Lunes
        if dia == "1":
            # Verificar día no repetido
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Error: el paciente ya tiene un turno ese día.")
            # Guardar en el primer espacio libre
            elif lunes1 == "":
                lunes1 = nombre
                print("Turno 1 reservado")
            elif lunes2 == "":
                lunes2 = nombre
                print("Turno 2 reservado.")
            elif lunes3 == "":
                lunes3 = nombre
                print("Turno 3 reservado.")
            elif lunes4 == "":
                lunes4 = nombre
                print("Turno 4 reservado.")
            else:
                print("Día Lunes completo.")

        # Día Martes
        elif dia == "2":
            # Verificar día no repetido
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error: el paciente ya tiene un turno ese día.")
            # Guardar en el primer espacio libre
            elif martes1 == "":
                martes1 = nombre
                print("Turno 1 reservado.")
            elif martes2 == "":
                martes2 = nombre
                print("Turno 2 reservado.")
            elif martes3 == "":
                martes3 = nombre
                print("Turno 3 reservado.")
            else:
                print("Día Martes completo.")
    # Opción: Cancelar turno
    elif opcion == "2":
        # Elegir y validar día
        dia = input("Elija día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 (Lunes) o 2 (Martes)")
            dia = input("Error. Elija día (1=Lunes, 2=Martes): ")
        # Nombre del paciente
        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error. Nombre del paciente: ")
        if dia == "1":
            if nombre == lunes1:
                lunes1 = ""
                print("Turno cancelado con éxito")
            elif nombre == lunes2:
                lunes2 = ""
                print("Turno cancelado con éxito")
            elif nombre == lunes3:
                lunes3 = ""
                print("Turno cancelado con éxito")
            elif nombre == lunes4:
                lunes4 = ""
                print("Turno cancelado con éxito")
            else:
                print("Paciente no encontrado")
        elif dia == "2":
            if nombre == martes1:
                martes1 = ""
                print("Turno cancelado con éxito")
            elif nombre == martes2:
                martes2 = ""
                print("Turno cancelado con éxito")
            elif nombre == martes3:
                martes3 = ""
                print("Turno cancelado con éxito")
            else:
                print("Paciente no encontrado")
    # Ver agenda del día
    elif opcion == "3":
        dia = input("Elija día (1=Lunes, 2=Martes): ")
        # Validación
        while dia != "1" and dia != "2":
            dia = input("Error. Elija día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Agenda del día Lunes")
            if lunes1 == "":
                print("Turno 1: libre")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: libre")
            else: 
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: libre")
            else:
                print("Turno 3:", lunes3)
            if lunes4 == "":
                print("Turno 4: libre")
            else:
                print("Turno 4:", lunes4)
        elif dia == "2":
            print("Agenda del día Martes")
            if martes1 == "":
                print("Turno 1: libre")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: libre")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: libre")
            else:
                print("Turno 3:", martes3)
    # Resumen general
    elif opcion == "4":
        # Sumatoria Lunes
        ocupados_lunes = 0
    
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        # Sumatoria Martes
        ocupados_martes = 0

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        # Días con más turnos
        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} libres")
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate" )
