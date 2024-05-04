import os, time, math
os.system("cls")

# Cantidades

cant_trad = 0
cant_pepe = 0
cant_all = 0
pagar = 0
dinero = 0
dinero_total = 0
vuelto = 0
descuento = 0
pagar_descuento = 0

menu = True
while menu:
    print("Hola, para comenzar ingresa tu horario de estudio")
    print("1. Horario Diurno")
    print("2. Horario Vespertino")
    print("3. Administrativos")

    try:
        opcion_menu = int(input("Ingrese una opcion: "))
    except:
        print("Ingrese un valor numerico")
        time.sleep(1)
        os.system("cls")
    
    if opcion_menu < 1 or opcion_menu> 3:
        print("Lo sentimos, ingrese una opcion valida")
        time.sleep(1)
        os.system("cls")
    
    else:

        if opcion_menu == 1:
            descuento = 0.12
        elif opcion_menu == 2:
            descuento = 0.1
        else:
            descuento = 0
    
    menu = False

menu_principal = True

while menu_principal:
    os.system("cls")
    print("=== Menú PizzaDuoc ===")
    print("1. Tienda")
    print("2. Carrito")
    print("3. Salir")

    try:
        opcion_menu_ppal = int(input("Ingrese una opcion: "))
    except:
        print("Ingrese un valor numerico")
        time.sleep(1)
        os.system("cls")
    
    if opcion_menu_ppal < 1 or opcion_menu_ppal > 3:
        print("Lo sentimos, ingrese una opcion valida")
        time.sleep(1)
        os.system("cls")
    
    else:

        if opcion_menu_ppal == 1:
            menu_comprar = True

            while menu_comprar:
                os.system("cls")
                print("=== Comprar ===")
                print("1. Pizza Tradicional\t$12000")
                print("2. Pizza Peperonni\t$14000")
                print("3. Pizza All Carnes\t$17000")
                print("4. Regresar")

                try:
                    opcion_menu_comprar = int(input("Ingrese una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")
                
                if opcion_menu_comprar < 1 or opcion_menu_comprar > 4:
                    print("Lo sentimos, ingrese una olcion valida")
                    time.sleep(1)
                    os.system("cls")
                
                else:

                    if opcion_menu_comprar == 1:
                        try:
                            cant_trad += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                    elif opcion_menu_comprar == 2:
                        try:
                            cant_pepe += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                    elif opcion_menu_comprar == 3:
                        try:
                            cant_all += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                    else:
                        menu_comprar = False
        
        elif opcion_menu_ppal == 2:

            

            menu_carrito = True
            while menu_carrito:
                os.system("cls")
                print("Productos:")
                if cant_trad > 0:
                    print(f"- Pizza Tradicional \tx{cant_trad}\t${math.trunc((cant_trad * 12000)*(1-descuento))}")
                if cant_pepe > 0:
                    print(f"- Pizza Peperonni \tx{cant_pepe}\t${math.trunc((cant_pepe * 14000)*(1-descuento))}")
                if cant_all > 0:
                    print(f"- Pizza All Carnes \tx{cant_all}\t${math.trunc((cant_all * 17000)*(1-descuento))}")
                print("=== Que deseas hacer? ===")
                print("1. Finalizar compra")
                print("2. Seguir comprando")

                try:
                    opcion_menu_carrito = int(input("Ingrese una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")
                
                if opcion_menu_carrito < 1 or opcion_menu_carrito > 2:
                    print("Lo sentimos, ingrese una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                
                else:

                    if opcion_menu_carrito == 1:
                        
                        if cant_trad + cant_pepe + cant_all != 0:
                            pagar = (12000 * cant_trad) + (14000 * cant_pepe) + (17000 * cant_all)
                            pagar_descuento = math.trunc(round((pagar - (pagar * descuento)),0))

                            while dinero_total < pagar_descuento:
                                os.system("cls")
                                deuda = pagar_descuento - dinero_total
                                print(f"Ud debe cancelar: ${deuda}")

                                try:
                                    dinero = int(input("Ingrese un monto a cancelar: "))
                                except:
                                    print("Ingrese un valor numerico")
                                    time.sleep(1)
                                    os.system("cls")

                                dinero_total += dinero
                            
                            vuelto = dinero_total - pagar_descuento
                            menu_principal = False
                            menu_carrito = False

                            print("      === Boleta ===")
                            print("--------------------------------")
                            print("Productos:")
                            if cant_trad > 0:
                                print(f"- Pizza Tradicional\t{cant_trad}")
                            if cant_pepe > 0:
                                print(f"- Pizza Peperonni\t{cant_pepe}")
                            if cant_all > 0:
                                print(f"- Pizza All Carnes\t{cant_all}")
                            print("---------------------------------")
                            print(f"Monto:\t\t${deuda}")
                            print(f"Descuento:\t${math.trunc(round((deuda*descuento),0))}")
                            print(f"Monto Final:\t${pagar_descuento}")
                            print(f"Pago:\t\t${dinero_total}")
                            print(f"Vuelto:\t\t${vuelto}")
                            print("---------------------------------")
                            print("== ¡Gracias por tu compra! ==")
                            break

                        else:
                            print("Debes comprar algo para poder pagarlo")
                            time.sleep(1.5)
                            os.system("cls")
                        os.system("cls")
                    
                    else:
                        menu_carrito = False
        elif opcion_menu_ppal == 3:
            print("Adios, vuelva pronto")
            time.sleep(2)
            menu_principal = False



