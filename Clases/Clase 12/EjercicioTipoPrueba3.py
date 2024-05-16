import os, time, math
os.system("cls")


cant_p1 = 0
cant_p2 = 0
cant_p3 = 0
cant_p4 = 0

cant_b1 = 0
cant_b2 = 0
cant_b3 = 0

subtotal = 0
totalFinal = 0

dineroFinal = 0
dinero = 0

descuento = 0

subtotales = []


# evaluar la lista para ver si antes se compro algo de mas de 50k


menu_ppal = True

while menu_ppal:

    for i in range(0,len(subtotales)):
        if subtotales[i] > 50000:
            descuento = 10


    os.system("cls")
    print("==== Que deseas hacer? ====")
    print("1. Comprar")
    print("2. Pagar")
    print("3. Anular Pedido")
    print("4. Salir")

    try:
        opcion_ppal = int(input("Ingrese una opcion: "))
    except:
        print("Ingrese un valor numerico")
        time.sleep("1")
        os.system("cls")
    
    if opcion_ppal < 1 or opcion_ppal > 4:
        print("Ingrese una opcion valida")
        time.sleep(1)
        os.system("cls")
    else:

        if opcion_ppal == 1:
            menu_comprar = True

            while menu_comprar:
                os.system("cls")
                print("=== Que deseas comprar? ===")
                print("1. Platos")
                print("2. Bebidas")
                print("3. Regresar")

                try:
                    opcion_comprar = int(input("Ingrese una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep("1")
                    os.system("cls")
                
                if opcion_comprar < 1 or opcion_comprar > 3:
                    print("Ingrese una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                else:

                    if opcion_comprar == 1:
                        menu_platos = True

                        while menu_platos:
                            os.system("cls")
                            print("=== Platos ===")
                            print("1. Curanto\t\t$20.000")
                            print("2. Mariscal\t\t$12.000")
                            print("3. Chupe Centolla\t$15.000")
                            print("4. Empanadas\t\t$3.000")
                            print("5. Regresar")

                            try:
                                opcion_platos = int(input("Ingrese una opcion: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep("1")
                                os.system("cls")

                            if opcion_platos < 1 or opcion_platos > 5:
                                print("Ingrese una opcion valida")
                                time.sleep(1)
                                os.system("cls")
                            else:

                                if opcion_platos == 1:
                                    try:
                                        cant_p1 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")
                                
                                elif opcion_platos == 2:
                                    try:
                                        cant_p2 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")

                                elif opcion_platos == 3:
                                    try:
                                        cant_p3 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")

                                elif opcion_platos == 4:
                                    try:
                                        cant_p4 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")
                                
                                else:
                                    menu_platos = False

                    elif opcion_comprar == 2:
                        menu_bebidas = True

                        while menu_bebidas:
                            os.system("cls")
                            print("=== Bebidas ===")
                            print("1. Pisco Sour\t\t$5.000")
                            print("2. Bebidas Lata\t\t$3.000")
                            print("3. Jugos Naturales\t\t$2.500")
                            print("4. Regresar")

                            try:
                                opcion_bebidas = int(input("Ingrese una opcion: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep("1")
                                os.system("cls")

                            if opcion_bebidas < 1 or opcion_bebidas > 4:
                                print("Ingrese una opcion valida")
                                time.sleep(1)
                                os.system("cls")
                            else:

                                if opcion_bebidas == 1:
                                    try:
                                        cant_b1 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")
                                
                                elif opcion_bebidas == 2:
                                    try:
                                        cant_b2 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")
                                        
                                elif opcion_bebidas == 3:
                                    try:
                                        cant_b3 += int(input("Cuantas deseas?: "))
                                    except:
                                        print("Ingrese un valor numerico")
                                        time.sleep("1")
                                        os.system("cls")
                                
                                else:
                                    menu_bebidas = False
                            
                    else:
                        menu_comprar = False

        elif opcion_ppal == 2:
            menu_pagar = True

            while menu_pagar:
                os.system("cls")
                print("=== Productos ===")
                if cant_p1 + cant_p2 + cant_p3 + cant_p4 > 0:
                    print("-- Platos --")
                    if cant_p1 > 0:
                        print(f"{cant_p1} Curanto\t${cant_p1*20000}")
                    if cant_p2 > 0:
                        print(f"{cant_p2} Mariscal\t${cant_p2*12000}")
                    if cant_p3 > 0:
                        print(f"{cant_p3} Chupe Centolla\t${cant_p3*15000}")
                    if cant_p4 > 0:
                        print(f"{cant_p4} Empanadas\t{cant_p4*3000}")
                if cant_b1 + cant_b2 + cant_b3 > 0:
                    print("-- Bebidas --")
                    if cant_b1 > 0:
                        print(f"{cant_b1} Pisco Sour\t${cant_b1*5000}")
                    if cant_b2 > 0:
                        print(f"{cant_b2} Bebidas Lata\t{cant_b2*3000}")
                    if cant_b3 > 0:
                        print(f"{cant_b3} Jugos Naturales\t${cant_b3*2500}")
                print("-"*40)
                print()
                print("=== Que deseas hacer? ===")
                print("1. Finalizar Compra")
                print("2. Seguir Comprando")

                try:
                    opcion_pagar = int(input("Selecciona una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep("1")
                    os.system("cls")
                
                if opcion_pagar < 1 or opcion_pagar > 2:
                    print("Ingrese una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                else:

                    if opcion_pagar == 1:
                        if (cant_p1 + cant_p2 + cant_p3 + cant_p4)+(cant_b1 + cant_b2 + cant_b3) <= 0:
                            print("Debes comprar algo para poder pagarlo")
                            time.sleep(1)
                            os.system("cls")
                        else:

                            subtotal = (cant_p1*20000)+(cant_p2*12000)+(cant_p3*15000)+(cant_p4*3000)+(cant_b1*5000) + (cant_b2*3000) + (cant_b3*2500)
                            totalFinal = subtotal - int(subtotal*descuento/100)

                            while dineroFinal < totalFinal:
                                os.system("cls")
                                deuda = totalFinal - dineroFinal
                                print(f"Ud. debe cancelar ${deuda}")

                                try:
                                    dinero = int(input("Ingrese el monto a cancelar: "))
                                except:
                                    print("Ingrese un valor numerico")
                                    time.sleep("1")
                                    os.system("cls")
                                
                                if dinero <= 0:
                                    print("Ingrese un monto valido")
                                    dinero = 0
                                    time.sleep(1)
                                
                                dineroFinal += dinero
                            
                            vuelto = dineroFinal - totalFinal
                            subtotales.append(subtotal)
                            menu_pagar = False
                            menu_ppal = False

                            #Boleta
                            os.system("cls")
                            print("-"*40)
                            print("Detalle de la compra")
                            print("-"*40)
                            if cant_p1 > 0:
                                print(f"- {cant_p1} Curanto\t${cant_p1*20000}")
                            if cant_p2 > 0:
                                print(f"- {cant_p2} Mariscal\t${cant_p2*12000}")
                            if cant_p3 > 0:
                                print(f"- {cant_p3} Chupe Centolla\t${cant_p3*15000}")
                            if cant_p4 > 0:
                                print(f"- {cant_p4} Empanadas\t${cant_p4*3000}")
                            if cant_b1 > 0:
                                print(f"- {cant_b1} Pisco Sour\t${cant_b1*5000}")
                            if cant_b2 > 0:
                                print(f"- {cant_b2} Bebidas Lata\t${cant_b2*3000}")
                            if cant_b3 > 0:
                                print(f"- {cant_b3} Jugos Naturales\t{cant_b3*2500}")
                            print("-"*40)
                            print(f"Subtotal\t\t${subtotal}")
                            print(f"Descuento {descuento}%\t\t${int(subtotal*descuento/100)}")
                            print("-"*40)
                            print(f"Total\t\t\t${totalFinal}")
                            print("-"*40)
                            print(f"Monto\t\t\t${dineroFinal}")
                            print(f"Vuelto\t\t\t${vuelto}")
                            print("-"*40)
                            print("Gracias por su compra!")
                            print(subtotales)




                    else:
                        menu_pagar = False

        elif opcion_ppal == 3:
            menu_ppal = False
        
        else:
            print("Adios!")
            menu_ppal = False
