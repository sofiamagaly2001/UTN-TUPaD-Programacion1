# Caja del kiosco
# Nombre del cliente
nombre = input("Nombre del cliente: ")

while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Nombre del cliente: ")

# Cantidad de productos
cantidad = input("Cantidad de productos a comprar: ")

while not cantidad.isdigit() or cantidad == "0":
    print("Error: ingrese un número mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0.0

# Productos
for i in range(cantidad):
    precio = input(f"Precio del producto {i+1}: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Precio del producto {i+1}: ")

    precio_final = int(precio)
    total_sin_descuentos += precio_final

    descuento_sn = input("¿Tiene descuento? (S/N): ").lower()

    while descuento_sn != "s" and descuento_sn != "n":
        print("Error: ingrese S o N.")
        descuento_sn = input("¿Tiene descuento? (S/N): ").lower()

    if descuento_sn == "s":
        precio_con_descuento = precio_final * 0.90
    else:
        precio_con_descuento = precio_final

    total_con_descuentos += precio_con_descuento

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

# Resultados
print(f"\nCliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")