import os, time
os.system("cls")

opcion = 0
menu = True

while menu:
    print("=== Tienda ===")
    print("1. Lapices \t\t $500")
    print("2. Goma de borrar \t $300")
    print("3. Sacapuntas \t\t $200")
    
    try:
        opcion = int(input("Ingrese una opcion: "))

    except:
        print("La opcion debe ser numerica")
        time.sleep(1)
        os.system("cls")

    if opcion < 1 or opcion > 3:
        print("Ingrese una opcion válida")
        time.sleep(1)
        os.system("cls")
    
    else:
        menu = False

valor_producto = 0
nombre_producto = ""

if opcion == 1:
    valor_producto = 500
    nombre_producto = "Lapices"

elif opcion == 2:
    valor_producto = 300
    nombre_producto = "Goma de borrar"

elif opcion == 3:
    valor_producto = 200
    nombre_producto = "Sacapuntas"
else:
    print("Error")


menu_dinero = True
vuelto = 0
dinero_total = 0
dinero = 0

while menu_dinero:
    print(f"Ud debe cancelar ${valor_producto}")

    try:
        dinero = int(input("Ingrese un monto a cancelar: "))
    except:
        print("Ingrese un monto válido")
        time.sleep(1)
        os.system("cls")
    dinero_total += dinero
    if dinero_total < valor_producto:
        print(f"A ud le falta cancelar: ${valor_producto - dinero_total}")
        input()
    else:
        vuelto = dinero_total - valor_producto
        menu_dinero = False


# Boleta

print("=======================")
print("\tBoleta")
print("=======================")
print("")
print(f"Producto: \t{nombre_producto}")
print(f"Valor: \t\t${valor_producto}")
print(f"Dinero: \t${dinero_total}")
print(f"Vuelto: \t${vuelto}")