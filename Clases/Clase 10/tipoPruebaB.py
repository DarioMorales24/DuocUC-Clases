import os, time, math
os.system("cls")


cant_menor = 0
cant_adulto = 0
cant_adultomayor = 0
descuento = 0
desc_menor = 0
desc_adulto = 0
subtotal = 0
totalfinal = 0
dinero = 0
dinero_total = 0
vuelto = 0

dia = True
while dia:
    print("Buenos días les desea el club 'Buena Ventura'.")
    print("Para comenzar responda a la siguiente pregunta")
    print("")
    print("Ingrese el día de hoy")

    opcion_dia = input("Escriba el día de hoy: ")
    dia_escogido = opcion_dia.upper()
    if dia_escogido == "VIERNES":
        desc_menor = 10
        desc_adulto = 5
        dia = False
    else:
        dia = False

menu = True

while menu:
    os.system("cls")

    print("=== Menú Entradas ===")
    print("1. Tienda")
    print("2. Carrito")
    print("3. Salir")

    try:
        opcion_menu = int(input("Ingrese una opcion: "))

    except:
        print("Ingrese un valor numerico")
        time.sleep(1)
        os.system("cls")

    if opcion_menu < 1 or opcion_menu > 3:
        print("Seleccione una opcion valida")
        time.sleep(1)
        os.system("cls")
    
    else:

        if opcion_menu == 1:

            menu_comprar = True

            while menu_comprar:
                os.system("cls")
                print("== Tipos de entrada ==")
                print("1. Menores (5-12 años)\t\t$2500")
                print("2. Adultos (13-64 años)\t\t$5000")
                print("3. Adultos Mayores (13-64 años)\t$5000")
                print("4. Anular Compra")
                print("5. Regresar")

                try:
                    opcion_comprar = int(input("Ingrese una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")

                if opcion_comprar < 1 or opcion_comprar > 5:
                    print("Ingrese una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                
                else:

                    if opcion_comprar == 1:
                        try:
                            cant_menor += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                    elif opcion_comprar == 2:
                        try:
                            cant_adulto += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                    elif opcion_comprar == 3:
                        try:
                            cant_adultomayor += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                    elif opcion_comprar == 4:
                        menu_comprar = False
                        menu = False
                        print("Adios, Vuelva pronto")


                    else:
                        menu_comprar = False
                    
        elif opcion_menu == 2:
            os.system("cls")

            menu_carrito = True
            while menu_carrito:
                print("Entradas:")
                if cant_menor + cant_adulto + cant_adultomayor > 0:
                    if cant_menor > 0:
                        print(f"Menores x{cant_menor}\t\t{cant_menor*2500}")
                    if cant_adulto > 0:
                        print(f"Adultos x{cant_adulto}\t\t{cant_adulto*5000}")
                    if cant_adultomayor > 0:
                        print(f"Adultos Mayores x{cant_adultomayor}\t{cant_adultomayor*1000}")
                else:
                    print("Tu carrito esta vacío")
                print("-"*30)
                print("=== Que deseas hacer? ===")
                print("1. Finalizar compra")
                print("2. Seguir comprando")

                try:
                    opcion_carrito = int(input("Ingresa una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")
                
                if opcion_carrito < 1 or opcion_carrito > 2:
                    print("Ingrese una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                else:

                    if opcion_carrito == 1 and (cant_adulto + cant_adultomayor + cant_menor != 0):

                        subtotal = cant_menor*2500 + cant_adulto*5000 + cant_adultomayor*1000
                        totalfinal = (cant_menor*2500)*(1-(desc_menor/100)) + (cant_adulto*5000)*(1-(desc_adulto/100)) + (cant_adultomayor*1000)

                        while dinero_total < totalfinal:
                            os.system("cls")
                            deuda = totalfinal - dinero_total
                            print(f"Ud debe cancelar: ${math.trunc(deuda)}")

                            try:
                                dinero = int(input("Ingrese un monto a cancelar: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep(1)
                                os.system("cls")

                            dinero_total += dinero

                        vuelto = dinero_total - totalfinal
                        menu_carrito = False
                        menu = False

                        #Boleta

                        if subtotal != 0:
                            print("-"*40)
                            print(f"\t\tEntradas")
                            print("-"*40)
                            if cant_menor > 0:
                                print(f"{cant_menor} entradas Menores \t\t ${cant_menor*2500}")
                            if cant_adulto > 0:
                                print(f"{cant_adulto} entradas Adultos \t\t ${cant_adulto*5000}")
                            if cant_adultomayor > 0:
                                print(f"{cant_adultomayor} entradas Adultos Mayores \t ${cant_adultomayor*1000}")
                            print("-"*40)
                            print(f"Subtotal: \t\t\t ${subtotal}")
                            print(f"Descuentos: \t\t\t ${math.trunc(subtotal-totalfinal)}")
                            print("-"*40)
                            print(f"Total a pagar: \t\t\t ${math.trunc(totalfinal)}")
                            print("-"*40)
                            print(f"Monto: \t\t\t\t ${dinero_total}")
                            print(f"Vuelto: \t\t\t ${math.trunc(vuelto)}")
                            print("     == ¡Gracias por tu compra! ==")
                        else:
                            print("Adios, Vuelva pronto")
                    elif opcion_carrito == 2:
                        menu_carrito = False
                    else:
                        print("elije algo para poder pagarlo")
                        time.sleep(1)
                        os.system("cls")
        else:
            print("Adios, Vuelva pronto")
            menu = False


