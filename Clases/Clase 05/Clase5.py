import os, time
os.system("cls")

"""choice = True

while choice:
    print("== Mascotas ==")
    print("1. Gato")
    print("2. Perro")
    print("3. Serpiente")
    try:                        # <- con try puedes ponerle excepciones para evitar que se caiga el programa por algun tipo de error
        pet = int(input("Ingrese una de las opciones: "))
        if pet < 1 or pet > 3:
            print("Escoja una opcion válida")
            time.sleep(2)
            os.system("cls")
        else:
            choice = False
    except:                     # <- con except puedes añadir comando por si existe una excepcion
        print("Ingrese una opcion numerica")
        time.sleep(1)
        os.system("cls")

if pet == 1:
    print("Ud escogió un Gato")
elif pet == 2:
    print("Ud escogió un Perro")
else:
    print("Ud escogió un Serpiente")"""

choice = True
valor = 0
producto = ""

while choice:
    print("== Bebidas ==")
    print("1. Cocacola \t $900")
    print("2. Pepsi \t $900")
    print("3. 7up \t\t $800")
    print("4. Fanta \t $850")
    print("5. Incacola \t $700")
    try:                        # <- con try puedes ponerle excepciones para evitar que se caiga el programa por algun tipo de error
        opcion = int(input("Ingrese una de las opciones: "))
        if opcion < 1 or opcion > 5:
            print("Escoja una opcion válida")
            time.sleep(2)
            os.system("cls")
        else:
            choice = False
    except:                     # <- con except puedes añadir comando por si existe una excepcion
        print("Ingrese una opcion numerica")
        time.sleep(1)
        os.system("cls")

if opcion == 1:
    valor = 900
    producto = "Coca-Cola"
elif opcion == 2:
    valor = 900
    producto = "Pepsi"
elif opcion == 3:
    valor = 800
    producto = "7up"
elif opcion == 4:
    valor = 850
    producto = "Fanta"
else:
    valor = 700
    producto = "Inca-Cola"

dinero = 0
dineroTotal = 0

print(f"Ud escogió una {producto} y debe cancelar ${valor}")
while dineroTotal < valor:
    try:
        dinero = int(input("Ingrese un monto a cancelar: "))
        dineroTotal += dinero
        if dineroTotal < valor:
            print(f"A ud le faltan: ${valor-dineroTotal}")
        else:
            print(f"Su vuelto es de: ${dineroTotal-valor}")
    except:
        print("Ingrese un valor numerico")
        time.sleep(1)
        os.system("cls")

print("--------------------------")
print(f"Aqui tienes tu {producto}")
print("--------------------------")
print("    == Boleta ==")
if opcion == 3 or opcion == 2 or opcion == 4:
    print(f"{producto} \t\t ${valor}")
else:
    print(f"{producto} \t ${valor}")
print(f"Efectivo: \t ${dineroTotal}")
print(f"Vuelto: \t ${dineroTotal-valor}")
print("= Gracias por su compra =")
print("--------------------------")


