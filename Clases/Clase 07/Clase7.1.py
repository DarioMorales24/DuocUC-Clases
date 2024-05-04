import os,time
os.system("cls")

poke_1_nombre = ""
poke_2_nombre = ""
poke_1_daño = 10
poke_2_daño = 11
poke_1_vida = 100
poke_2_vida = 100
menu_seleccion = True
opcion_menu_selecion = 0
nombre = input("Ingresa tu nombre: ")
print(f"Hola, joven {nombre} bienvenido al mundo de los pokemons")
input("(Presiona enter para continuar)")
print("En este mundo habitan criaturas llamadas Pokemons")
input("(Presiona enter para continuar)")
print(f"Bueno {nombre}, es hora que comiences tu aventura")
input("(Presiona enter para continuar)")
print(f"Bienvenido {nombre}, para comenzar escoje uno de estos pokemons")
input("(Presiona enter para continuar)")

while menu_seleccion:
    print("1. Bulbasaur (El pokemon tipo Planta)")
    print("2. Squirtle (El pokemon tipo Agua)")
    print("3. Charmander (El pokemon tipo Fuego)")
    
    try:
        opcion_menu_selecion = int(input("Ingrese una opcion: "))
    except:
        print("Ingresa una opcion válida.")
        time.sleep(1)
        os.system("cls")

    if opcion_menu_selecion < 1 or opcion_menu_selecion > 3:
        print("Ingrese una opcion válida")
        time.sleep(1)
        os.system("cls")
    else:
        menu_seleccion = False

if opcion_menu_selecion == 1:
    poke_1_nombre = "Bulbasaur"
    poke_2_nombre = "Charmander"

elif opcion_menu_selecion == 2:
    poke_1_nombre = "Squirtle"
    poke_2_nombre = "Bulbasaur"

else:
    poke_1_nombre = "Charmander"
    poke_2_nombre = "Squirtle"

