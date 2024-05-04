import os, time # <- time es una libreria para poner esperar
os.system("cls") # <- este es para borrar pantalla

# While

"""menu = True

while menu:
    print("Bebidas:")
    print("1. Cocacola\t $900")
    print("2. Pepsi\t $800")
    print("3. Inkacola\t $700")
    opcion = int(input("Ingresa una de las opciones: "))

    if opcion < 1 or opcion > 3:
        print("Elija una opcion valida")
        time.sleep(2)
        os.system("cls")
    else:
        menu = False

if opcion == 1:
    print("Eligió Cocacola")
elif opcion == 2:
    print("Eligió Pepsi")
elif opcion == 3:
    print("Eligió Inkacola")
else:
    print("Error")"""


# FOR


for i in range(6):
    print(f"Repitiendo x veces {i}")

print("------------------------------------------")     

for i in range(5, 10): # podemos ponerle rangos a los range, y al final de cuantos se mueve 
    print(f"Repitiendo x veces {i}")

print("------------------------------------------")     
for i in range(0, 10, 2): # <- range({inicio},{final-1},{cantidad de saltos})  <- esta es la sintaxis del range
    print(f"Repitiendo x veces {i}")