import os, time, random
os.system("cls")

# Cantidades RP
cant_rp1 = 0
cant_rp2 = 0
cant_rp3 = 0
cant_rp4 = 0
cant_rp5 = 0
cant_rp6 = 0
rp = 0
# Campeones
campeones = []

menu_principal = True

while menu_principal:
# =======================================================================================================================
# ===================================================== MENU PRINCIPAL ==================================================
# =======================================================================================================================

    os.system("cls")
    print("=== Menú Principal ===")
    print("1. Tienda")
    print("2. Coleccion")
    print("3. Salir")

    try:
        opcion_menu_principal = int(input("Seleccione una opcion: "))
    except:
        print("Ingrese una opcion numerica")
        time.sleep(1)
        os.system("cls")

    if opcion_menu_principal < 1 or opcion_menu_principal > 3:
        print("Ingrese una opcion válida")
        time.sleep(1)
        os.system("cls")
    
    else:

# =======================================================================================================================
# ===================================================== MENU TIENDA =====================================================
# =======================================================================================================================

        if opcion_menu_principal == 1:

            menu_tienda = True

            while menu_tienda:
                os.system("cls")
                print("== Comprar ==")
                print("1. Riot Points")
                print("2. Campeones")
                print("3. Skins")
                print("4. Regresar al menú principal")

                try:
                    opcion_menu_tienda = int(input("Seleccione una opcion: "))
                except:
                    print("Ingrese una opcion numerica")
                    time.sleep(1)
                    os.system("cls")

                if opcion_menu_tienda < 1 or opcion_menu_tienda > 4:
                    print("Seleccione una opcion válida")
                    time.sleep(1)
                    os.system("cls")
                else:

                    if opcion_menu_tienda == 1:
                        
# =======================================================================================================================
# ===================================================== MENU RP =========================================================
# =======================================================================================================================

                        menu_rp = True
                        while menu_rp:
                            os.system("cls")
                            print("=========================")
                            print(f"\tRP = {rp}")
                            print("=========================")
                            print("1. 450 RP \t $2000")
                            print("2. 940 RP \t $4000")
                            print("3. 1950 RP \t $8000")
                            print("4. 3750 RP \t $15000")
                            print("5. 7800 RP \t $30000")
                            print("6. 13750 RP \t $50000")
                            print("7. Regresar")

                            try: 
                                opcion_menu_tienda_rp = int(input("Seleccione una opcion: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep(1)
                                os.system("cls")
                            
                            if opcion_menu_tienda_rp < 1 or opcion_menu_tienda_rp > 7:
                                print("Seleccione una opcion valida")
                                time.sleep(1)
                                os.system("cls")
                            else:

                                if opcion_menu_tienda_rp == 1:
                                    cant_rp1 += int(input("Ingrese la cantidad que desea:"))
                                    rp += (450*cant_rp1)
                                elif opcion_menu_tienda_rp == 2:
                                    cant_rp2 += int(input("Ingrese la cantidad que desea: "))
                                    rp += (940*cant_rp2)
                                elif opcion_menu_tienda_rp == 3:
                                    cant_rp3 += int(input("Ingrese la cantidad que desea: "))
                                    rp += (1950*cant_rp3)
                                elif opcion_menu_tienda_rp == 4:
                                    cant_rp4 += int(input("Ingrese la cantidad que desea: "))
                                    rp += (3750*cant_rp4)
                                elif opcion_menu_tienda_rp == 5:
                                    cant_rp5 += int(input("Ingrese la cantidad que desea: "))
                                    rp += (7800*cant_rp5)
                                elif opcion_menu_tienda_rp == 6:
                                    cant_rp6 += int(input("Ingrese la cantidad que desea: "))
                                    rp += (13750*cant_rp6)
                                else:
                                    menu_rp = False

                    elif opcion_menu_tienda == 2:
                        

                        menu_campeones = True

# =======================================================================================================================
# ===================================================== MENU CAMPEONES ==================================================
# =======================================================================================================================

                        while menu_campeones:
                            os.system("cls")
                            print("=========================")
                            print(f"\tRP = {rp}")
                            print("=========================")
                            print("1. Asesinos")
                            print("2. Luchadores")
                            print("3. Magos")
                            print("4. Tirador")
                            print("5. Tanque")
                            print("6. Soporte")
                            print("7. Regresar")

                            try: 
                                opcion_menu_tienda_campeones = int(input("Seleccione una opcion: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep(1)
                                os.system("cls")
                            
                            if opcion_menu_tienda_campeones < 1 or opcion_menu_tienda_campeones > 7:
                                print("Seleccione una opcion valida")
                                time.sleep(1)
                                os.system("cls")
                            else:

                                if opcion_menu_tienda_campeones == 1:
                                    os.system("cls")
                                    menu_asesinos = True

# =======================================================================================================================
# ===================================================== MENU ASESINOS ===================================================
# =======================================================================================================================

                                    while menu_asesinos:
                                        os.system("cls")
                                        print("=========================")
                                        print(f"\tRP = {rp}")
                                        print("=========================")
                                        print("1. Evelynn \t 585 RP")
                                        print("2. Fiddlestick \t 585 RP")
                                        print("3. Katarina \t 790 RP")
                                        print("4. Nidalee \t 790 RP")
                                        print("5. Shaco \t 790 RP")
                                        print("6. Regresar")

                                        try: 
                                            opcion_menu_tienda_campeones_asesinos = int(input("Seleccione una opcion: "))
                                        except:
                                            print("Ingrese un valor numerico")
                                            time.sleep(1)
                                            os.system("cls")
                                        
                                        if opcion_menu_tienda_campeones_asesinos < 1 or opcion_menu_tienda_campeones_asesinos > 7:
                                            print("Seleccione una opcion valida")
                                            time.sleep(1)
                                            os.system("cls")
                                        else:
                                            if opcion_menu_tienda_campeones_asesinos == 1:
                                                if rp >= 585:
                                                    if "Evelynn" in campeones:
                                                        print("Ya tienes a Evelynn en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Evelynn")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Evelynn a sido ingresada a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")
                                            
                                            elif opcion_menu_tienda_campeones_asesinos == 2:
                                                if rp >= 585:
                                                    if "Fiddlestick" in campeones:
                                                        print("Ya tienes a Fiddlestick en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Fiddlestick")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Fiddlestick a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_asesinos == 3:
                                                if rp >= 790:
                                                    if "Katarina" in campeones:
                                                        print("Ya tienes a Katarina en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Katarina")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Katarina a sido ingresada a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_asesinos == 4:
                                                if rp >= 790:
                                                    if "Nidalee" in campeones:
                                                        print("Ya tienes a Nidalee en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Nidalee")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Nidalee a sido ingresada a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_asesinos == 5:
                                                if rp >= 790:
                                                    if "Shaco" in campeones:
                                                        print("Ya tienes a Shaco en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Shaco")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Shaco a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")
                                            else:
                                                menu_asesinos = False

# =======================================================================================================================
# =================================================== MENU LUCHADORES ===================================================
# =======================================================================================================================

                                elif opcion_menu_tienda_campeones == 2:
                                    os.system("cls")
                                    menu_luchadores = True

                                    while menu_luchadores:
                                        os.system("cls")
                                        print("=========================")
                                        print(f"\tRP = {rp}")
                                        print("=========================")
                                        print("1. Dr. Mundo \t 260 RP")
                                        print("2. Maestro Yi \t 260 RP")
                                        print("3. Malphite \t 260 RP")
                                        print("4. Warwick \t 260 RP")
                                        print("5. Jax \t\t 585 RP")
                                        print("6. Sion \t 585 RP")
                                        print("7. Taric \t 585 RP")
                                        print("8. Tryndamere \t 585 RP")
                                        print("9. Udir \t 585 RP")
                                        print("10. Blitzcrank \t 790 RP")
                                        print("11. Gangplank \t 790 RP")
                                        print("12. Regresar")

                                        try: 
                                            opcion_menu_tienda_campeones_luchadores = int(input("Seleccione una opcion: "))
                                        except:
                                            print("Ingrese un valor numerico")
                                            time.sleep(1)
                                            os.system("cls")
                                        
                                        if opcion_menu_tienda_campeones_luchadores < 1 or opcion_menu_tienda_campeones_luchadores > 12:
                                            print("Seleccione una opcion valida")
                                            time.sleep(1)
                                            os.system("cls")
                                        else:
                                            if opcion_menu_tienda_campeones_luchadores == 1:
                                                if rp >= 260:
                                                    if "Dr. Mundo" in campeones:
                                                        print("Ya tienes a Dr. Mundo en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Dr. Mundo")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Dr. Mundo a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")
                                            
                                            elif opcion_menu_tienda_campeones_luchadores == 2:
                                                if rp >= 260:
                                                    if "Maestro Yi" in campeones:
                                                        print("Ya tienes a Maestro Yi en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Maestro Yi")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Maestro Yi a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 3:
                                                if rp >= 260:
                                                    if "Malphite" in campeones:
                                                        print("Ya tienes a Malphite en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Malphite")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Malphite a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 4:
                                                if rp >= 260:
                                                    if "Warwick" in campeones:
                                                        print("Ya tienes a Warwick en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Warwick")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Warwick a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 5:
                                                if rp >= 585:
                                                    if "Jax" in campeones:
                                                        print("Ya tienes a Jax en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Jax")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Jax a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 6:
                                                if rp >= 585:
                                                    if "Sion" in campeones:
                                                        print("Ya tienes a Sion en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Sion")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Sion a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 7:
                                                if rp >= 585:
                                                    if "Taric" in campeones:
                                                        print("Ya tienes a Taric en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Taric")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Taric a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 8:
                                                if rp >= 585:
                                                    if "Tryndamere" in campeones:
                                                        print("Ya tienes a Tryndamere en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Tryndamere")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Tryndamere a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 9:
                                                if rp >= 585:
                                                    if "Udir" in campeones:
                                                        print("Ya tienes a Udir en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Udir")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Udir a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 10:
                                                if rp >= 790:
                                                    if "Blitzcrank" in campeones:
                                                        print("Ya tienes a Blitzcrank en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Blitzcrank")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Blitzcrank a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_luchadores == 11:
                                                if rp >= 790:
                                                    if "Gangplank" in campeones:
                                                        print("Ya tienes a Gangplank en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Gangplank")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Gangplank a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")
                                            else:
                                                menu_luchadores = False

# =======================================================================================================================
# =================================================== MENU MAGOS ========================================================
# =======================================================================================================================


                                elif opcion_menu_tienda_campeones == 3:
                                    os.system("cls")
                                    menu_magos = True

                                    while menu_magos:
                                        os.system("cls")
                                        print("=========================")
                                        print(f"\tRP = {rp}")
                                        print("=========================")
                                        print("1. Amumu \t 260 RP")
                                        print("2. Annie \t 260 RP")
                                        print("3. Soraka \t 260 RP")
                                        print("4. Twisted Fate \t 260 RP")
                                        print("5. Cho'gath \t 585 RP")
                                        print("6. Evelynn \t 585 RP")
                                        print("7. Fiddlestick \t 585 RP")
                                        print("8. Janna \t 585 RP")
                                        print("9. Morgana \t 585 RP")
                                        print("10. Veigar \t 585 RP")
                                        print("11. Zilean \t 585 RP")
                                        print("12. Anivia \t 790 RP")
                                        print("13. Karthus \t 790 RP")
                                        print("14. Kassadin \t 790 RP")
                                        print("15. Katarina \t 790 RP")
                                        print("16. Nidalee \t 790 RP")
                                        print("17. Regresar")

                                        try: 
                                            opcion_menu_tienda_campeones_magos = int(input("Seleccione una opcion: "))
                                        except:
                                            print("Ingrese un valor numerico")
                                            time.sleep(1)
                                            os.system("cls")
                                        
                                        if opcion_menu_tienda_campeones_magos < 1 or opcion_menu_tienda_campeones_magos > 17:
                                            print("Seleccione una opcion valida")
                                            time.sleep(1)
                                            os.system("cls")
                                        else:
                                            if opcion_menu_tienda_campeones_magos == 1:
                                                if rp >= 260:
                                                    if "Amumu" in campeones:
                                                        print("Ya tienes a Amumu en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Amumu")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Amumu a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 2:
                                                if rp >= 260:
                                                    if "Annie" in campeones:
                                                        print("Ya tienes a Annie en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Annie")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Annie a sido ingresada a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 3:
                                                if rp >= 260:
                                                    if "Soraka" in campeones:
                                                        print("Ya tienes a Soraka en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Soraka")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Soraka a sido ingresada a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 4:
                                                if rp >= 260:
                                                    if "Twisted Fate" in campeones:
                                                        print("Ya tienes a Twisted Fate en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Twisted Fate")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Twisted Fate a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 5:
                                                if rp >= 585:
                                                    if "Cho'gath" in campeones:
                                                        print("Ya tienes a Cho'gath en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Cho'gath")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Cho'gath a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 6:
                                                if rp >= 585:
                                                    if "Evelynn" in campeones:
                                                        print("Ya tienes a Evelynn en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Evelynn")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Evelynn a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 7:
                                                if rp >= 585:
                                                    if "Fiddlestick" in campeones:
                                                        print("Ya tienes a Fiddlestick en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Fiddlestick")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Fiddlestick a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 8:
                                                if rp >= 585:
                                                    if "Janna" in campeones:
                                                        print("Ya tienes a Janna en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Janna")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Janna a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 9:
                                                if rp >= 585:
                                                    if "Morgana" in campeones:
                                                        print("Ya tienes a Morgana en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Morgana")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Morgana a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 10:
                                                if rp >= 585:
                                                    if "Veigar" in campeones:
                                                        print("Ya tienes a Veigar en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Veigar")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Veigar a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 11:
                                                if rp >= 585:
                                                    if "Zilean" in campeones:
                                                        print("Ya tienes a Zilean en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Zilean")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Zilean a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 12:
                                                if rp >= 790:
                                                    if "Anivia" in campeones:
                                                        print("Ya tienes a Anivia en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Anivia")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Anivia a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 13:
                                                if rp >= 790:
                                                    if "Karthus" in campeones:
                                                        print("Ya tienes a Karthus en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Karthus")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Karthus a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 14:
                                                if rp >= 790:
                                                    if "Kassadin" in campeones:
                                                        print("Ya tienes a Kassadin en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Kassadin")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Kassadin a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 15:
                                                if rp >= 790:
                                                    if "Katarina" in campeones:
                                                        print("Ya tienes a Katarina en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Katarina")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Katarina a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            if opcion_menu_tienda_campeones_magos == 15:
                                                if rp >= 790:
                                                    if "Nidalee" in campeones:
                                                        print("Ya tienes a Nidalee en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Nidalee")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Nidalee a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")
                                            
                                            else:
                                                menu_magos = False


# =======================================================================================================================
# =================================================== MENU Tiradores ====================================================
# =======================================================================================================================

                                elif opcion_menu_tienda_campeones == 4:
                                    os.system("cls")
                                    menu_tiradores = True

                                    while menu_tiradores:
                                        os.system("cls")
                                        print("=========================")
                                        print(f"\tRP = {rp}")
                                        print("=========================")
                                        print("1. Ashe \t 260 RP")
                                        print("2. Sivir \t 260 RP")
                                        print("3. Teemo \t 260 RP")
                                        print("4. Tristana \t 585 RP")
                                        print("5. Corki \t 790 RP")
                                        print("6. Twitch \t 790 RP")
                                        print("7. Regresar")

                                        try: 
                                            opcion_menu_tienda_campeones_tiradores = int(input("Seleccione una opcion: "))
                                        except:
                                            print("Ingrese un valor numerico")
                                            time.sleep(1)
                                            os.system("cls")
                                        
                                        if opcion_menu_tienda_campeones_tiradores < 1 or opcion_menu_tienda_campeones_tiradores > 7:
                                            print("Seleccione una opcion valida")
                                            time.sleep(1)
                                            os.system("cls")
                                        else:
                                            if opcion_menu_tienda_campeones_tiradores == 1:
                                                if rp >= 260:
                                                    if "Ashe" in campeones:
                                                        print("Ya tienes a Ashe en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Ashe")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Ashe a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_tiradores == 2:
                                                if rp >= 260:
                                                    if "Sivir" in campeones:
                                                        print("Ya tienes a Sivir en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Sivir")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Sivir a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_tiradores == 3:
                                                if rp >= 260:
                                                    if "Teemo" in campeones:
                                                        print("Ya tienes a Teemo en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Teemo")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Teemo a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_tiradores == 4:
                                                if rp >= 585:
                                                    if "Tristana" in campeones:
                                                        print("Ya tienes a Tristana en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Tristana")
                                                        campeones.sort()
                                                        rp = rp - 585
                                                        print("Tristana a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_tiradores == 5:
                                                if rp >= 790:
                                                    if "Corki" in campeones:
                                                        print("Ya tienes a Corki en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Corki")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Corki a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                            elif opcion_menu_tienda_campeones_tiradores == 6:
                                                if rp >= 790:
                                                    if "Twitch" in campeones:
                                                        print("Ya tienes a Twitch en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Twitch")
                                                        campeones.sort()
                                                        rp = rp - 790
                                                        print("Corki a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

                                elif opcion_menu_tienda_campeones == 5:
                                    os.system("cls")
                                    menu_tanques = True

                                    while menu_tanques:
                                        os.system("cls")
                                        print("=========================")
                                        print(f"\tRP = {rp}")
                                        print("=========================")
                                        print("1. Dr. Mundo \t 260 RP")
                                        print("2. Maestro Yi \t 260 RP")
                                        print("3. Malphite \t 260 RP")
                                        print("4. Warwick \t 260 RP")
                                        print("5. Jax \t\t 585 RP")
                                        print("6. Sion \t 585 RP")
                                        print("7. Taric \t 585 RP")
                                        print("8. Tryndamere \t 585 RP")
                                        print("9. Udir \t 585 RP")
                                        print("10. Blitzcrank \t 790 RP")
                                        print("11. Gangplank \t 790 RP")
                                        print("12. Gangplank \t 790 RP")
                                        print("13. Gangplank \t 790 RP")
                                        print("14. Regresar")

                                        try: 
                                            opcion_menu_tienda_campeones_luchadores = int(input("Seleccione una opcion: "))
                                        except:
                                            print("Ingrese un valor numerico")
                                            time.sleep(1)
                                            os.system("cls")
                                        
                                        if opcion_menu_tienda_campeones_luchadores < 1 or opcion_menu_tienda_campeones_luchadores > 12:
                                            print("Seleccione una opcion valida")
                                            time.sleep(1)
                                            os.system("cls")
                                        else:
                                            if opcion_menu_tienda_campeones_luchadores == 1:
                                                if rp >= 260:
                                                    if "Dr. Mundo" in campeones:
                                                        print("Ya tienes a Dr. Mundo en tus campeones")
                                                        time.sleep(2)
                                                    else:
                                                        campeones.append("Dr. Mundo")
                                                        campeones.sort()
                                                        rp = rp - 260
                                                        print("Dr. Mundo a sido ingresado a tu lista de Campeones")
                                                        time.sleep(2)
                                                        
                                                else:
                                                    print("No posees el suficiente RP para comprar a este campeon")
                                                    time.sleep(2)
                                                os.system("cls")

