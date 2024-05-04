import os, time
os.system("cls")




# Pantalones
cant_pantalones_corto = 0
cant_pantalones_largo = 0
cant_pantalones_jeans = 0

# poleras
cant_poleras_larga = 0
cant_poleras_corta = 0
cant_poleras_tirante = 0

# Polerones

cant_polerones_corto = 0
cant_polerones_largo = 0
cant_polerones_sin = 0

menu_ppal = True
while menu_ppal:
    print("== Tipo ==")
    print("1. Pantalones")
    print("2. Poleras")
    print("3. Polerones")
    print("4. Boleta")
    print("5. Adios")

    opcion_menu = 0 

    try:
        opcion_menu = int(input("Ingrese una opcion: "))
    except:
        print("Ingrese un valor numerico")    

    if opcion_menu < 1 or opcion_menu > 5:
        print("La opcion ingresada no esta disponible")
        time.sleep(1)
        os.system("cls")
    else:
        os.system("cls")    
        if opcion_menu == 1:
            menu_pantalones = True
            while menu_pantalones:
                print("== Pantalones ==")
                print("1. Corto")
                print("2. Largo")
                print("3. Jeans")
                print("4. Regresar")
                
                opcion_pantalones = 0
                try:
                    opcion_pantalones = int(input("Seleccione una opcion: "))
                except:
                    print("Ingrese un valor numerico")

                if opcion_pantalones < 1 or opcion_pantalones > 4:
                    print("La opcion ingresada no esta disponible")
                    time.sleep(1)
                    os.system("cls")

                else:
                        
                    if opcion_pantalones == 1:
                        cant_pantalones_corto += int(input("Ingrese la cantidad de pantalones cortos que desea: "))
                    elif opcion_pantalones == 2:
                        cant_pantalones_largo += int(input("Ingrese la cantidad de pantalones largos que desea: "))
                    elif opcion_pantalones == 3:
                        cant_pantalones_jeans += int(input("Ingrese la cantidad de Jeans que desea: "))
                    elif opcion_pantalones == 4:
                        menu_pantalones = False
                os.system("cls")

        elif opcion_menu == 2:
            menu_poleras = True
            while menu_poleras:
                print("== Poleras ==")
                print("1. Manga Corta")
                print("2. Manga Larga")
                print("3. Sin Manga")
                print("4. Regresar")
                    
                opcion_poleras = 0
                try:
                    opcion_poleras = int(input("Seleccione una opcion: "))
                except:
                    print("Ingrese un valor numerico")

                if opcion_poleras < 1 or opcion_poleras > 4:
                    print("La opcion ingresada no esta disponible")
                    time.sleep(1)
                    os.system("cls")

                else:
                            
                    if opcion_poleras == 1:
                        cant_poleras_corta += int(input("Ingrese la cantidad de poleras mangas cortas que desea: "))
                    elif opcion_poleras == 2:
                        cant_poleras_larga += int(input("Ingrese la cantidad de poleras mangas largas que desea: "))
                    elif opcion_poleras == 3:
                        cant_poleras_tirante += int(input("Ingrese la cantidad de poleras sin mangas que desea: "))
                    elif opcion_poleras == 4:
                        menu_pantalones = False
                    os.system("cls")

        elif opcion_menu == 3:
            menu_polerones = True
            while menu_polerones:
                print("== Polerones ==")
                print("1. Manga Corta")
                print("2. Manga Larga")
                print("3. Sin Mangas")
                print("4. Regresar")
                
                opcion_polerones = 0
                try:
                    opcion_polerones = int(input("Seleccione una opcion: "))
                except:
                    print("Ingrese un valor numerico")

                    if opcion_polerones < 1 or opcion_polerones > 4:
                        print("La opcion ingresada no esta disponible")
                        time.sleep(1)
                        os.system("cls")

                    else:
                        
                        if opcion_polerones == 1:
                            cant_polerones_corto += int(input("Ingrese la cantidad de polerones manga corta que desea: "))
                        elif opcion_polerones == 2:
                            cant_polerones_largo += int(input("Ingrese la cantidad de polerones manga larga que desea: "))
                        elif opcion_pantalones == 3:
                            cant_polerones_sin += int(input("Ingrese la cantidad de polerones sin manga que desea: "))
                        elif opcion_polerones == 4:
                            menu_pantalones = False
                    os.system("cls")
        elif opcion_menu == 4:
            print("=============== BOLETA =============")
        else:
            print("Adios, Vuelva pronto")
