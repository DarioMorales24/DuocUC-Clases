import os, time, math
os.system("cls")

cant_m1 = 0
cant_m2 = 0
cant_m3 = 0
cant_m4 = 0
cant_m5 = 0
descuento = 0
subtotal = 0
totalfinal = 0
dinero = 0
dinero_total = 0
vuelto = 0
nom_desc = ""


menu_ppal = True

print("Bienvenida/o a Shin Whe Wensha")
print("Esperamos que disfrute su comida")
time.sleep(2)
while menu_ppal:
    os.system("cls")
    print("=== ¿Que deseas hacer? ===")
    print("1. Tienda")
    print("2. Carrito")
    print("3. Salir")

    try:
        opcion_menu_ppal = int(input("Seleccione una opcion: "))
    except:
        print("Ingrese un valor numerico")
        time.sleep(1)
        os.system("cls")

    if opcion_menu_ppal < 1 or opcion_menu_ppal > 3:
        print("Seleccione una opcion valida")
        time.sleep(1)
        os.system("cls")
    
    else:
        if opcion_menu_ppal == 1:
            menu_comprar = True

            while menu_comprar:
                os.system("cls")
                print(f"\t== Menú ==")
                print("1. Camarón Mandarín\t$11.000")
                print("2. Carne Mongoliana\t$10.000")
                print("3. Chapsui Pollo\t$9.500")
                print("4. Chapsui Carne\t$12.000")
                print("5. Parrillada China\t$15.000")
                print("6. Regresar")
                print("7. Anular Pedido")

                try:
                    opcion_menu_comprar = int(input("Seleccione una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")

                if opcion_menu_comprar < 1 or opcion_menu_comprar > 7:
                    print("Seleccione una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                else:
                    if opcion_menu_comprar == 1:
                        try:
                            cant_m1 += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                        if cant_m1 < 0:
                            cant_m1 = 0
                            print("Ingrese una cantidad valida")
                            time.sleep(1)
                    
                    elif opcion_menu_comprar == 2:
                        try:
                            cant_m2 += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                        if cant_m2 < 0:
                            cant_m2 = 0
                            print("Ingrese una cantidad valida")
                            time.sleep(1)

                    elif opcion_menu_comprar == 3:
                        try:
                            cant_m3 += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                        if cant_m3 < 0:
                            cant_m3 = 0
                            print("Ingrese una cantidad valida")
                            time.sleep(1)

                    elif opcion_menu_comprar == 4:
                        try:
                            cant_m4 += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")
                        
                        if cant_m4 < 0:
                            cant_m4 = 0
                            print("Ingrese una cantidad valida")
                            time.sleep(1)

                    elif opcion_menu_comprar == 5:
                        try:
                            cant_m5 += int(input("Cuantas deseas?: "))
                        except:
                            print("Ingrese un valor numerico")
                            time.sleep(1)
                            os.system("cls")

                        if cant_m5 < 0:
                            cant_m5 = 0
                            print("Ingrese una cantidad valida")
                            time.sleep(1)

                    elif opcion_menu_comprar == 6:
                        menu_comprar = False

                    else:
                        os.system("cls")
                        menu_anular = True

                        while menu_anular:
                            print("¿Realmente quieres cancelar el pedido?")
                            print("1. Si")
                            print("2. No")

                            try:
                                opcion_menu_anular = int(input("Seleccione una opcion: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep(1)
                                os.system("cls")
                            
                            if opcion_menu_anular < 1 or opcion_menu_anular > 2:
                                print("Ingrese una opcion valida")
                                time.sleep(1)
                                os.system("cls")
                            else:
                                if opcion_menu_anular == 1:
                                    menu_anular = False
                                    menu_comprar = False
                                    menu_ppal = False
                                    print("Pedido anulado")
                                else:
                                    menu_anular = False
                                    menu_comprar = False


        elif opcion_menu_ppal == 2:
            os.system("cls")
            if cant_m1 + cant_m2 + cant_m3 + cant_m4 + cant_m5 != 0:
                menu_desc = True
                while menu_desc:
                    print("    == Descuentos ==")
                    print(f"1. Cliente Frecuente\t15%")
                    print(f"2. Tarjeta Vecino\t10%")
                    print(f"3. Carnet Tercera Edad\t7%")
                    print("4. No poseo descuento")

                    try:
                        opcion_menu_desc = int(input("Selecciona tu descuento: "))
                    except:
                        print("Ingrese un valor numerico")
                        time.sleep(1)
                        os.system("cls")

                    if opcion_menu_desc < 1 or opcion_menu_desc > 4:
                        print("Ingrese una opcion valida")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        if opcion_menu_desc == 1:
                            descuento = 15
                            nom_desc = "Cliente Frecuente"
                        elif opcion_menu_desc == 2:
                            descuento = 10
                            nom_desc = "Tarjeta Vecino"
                        elif opcion_menu_desc == 3:
                            descuento = 7
                            nom_desc = "Carnet Tercera Edad"
                        else:
                            menu_desc = False
                        menu_desc = False


            os.system("cls")
            menu_carrito = True

            while menu_carrito:
                print("\t\tCarrito")
                print("-"*40)
                if cant_m1 != 0:
                    print(f"Camarón Mandarín x{cant_m1}\t${cant_m1*11000}")
                if cant_m2 != 0:
                    print(f"Carne Mongoliana x{cant_m2}\t${cant_m2*10000}")
                if cant_m3 != 0:
                    print(f"Chapsui Pollo x{cant_m3}\t${cant_m3*9500}")
                if cant_m4 != 0:
                    print(f"Chapsui Carne x{cant_m4}\t${cant_m4*12000}")
                if cant_m5 != 0:
                    print(f"Parrillada China x{cant_m5}\t${cant_m5*15000}")
                if cant_m1 + cant_m2 + cant_m3 + cant_m4 + cant_m5 == 0:
                    print("Tu carrito está vacío")
                print("-"*40)
                
                print("-"*40)
                print("\t== ¿Que deseas hacer? ==")
                print("1. Finalizar Compra")
                print("2. Seguir Comprando")

                try:
                    opcion_menu_carrito = int(input("Seleccione una opcion: "))
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")

                if opcion_menu_carrito < 1 or opcion_menu_carrito > 2:
                    print("Ingrese una opcion valida")
                    time.sleep(1)
                    os.system("cls")
                else:
                    if opcion_menu_carrito == 1:
                        subtotal = (cant_m1*11000) + (cant_m2*10000) + (cant_m3*9500) + (cant_m4*12000) + (cant_m5 * 15000)
                        totalfinal = subtotal - (subtotal * (descuento/100))

                        while dinero_total < totalfinal:
                            os.system("cls")
                            deuda = totalfinal - dinero_total
                            print(f"Ud. debe cancelar: ${math.trunc(deuda)}")

                            try:
                                dinero = int(input("¿Cual es el monto a ingresar?: "))
                            except:
                                print("Ingrese un valor numerico")
                                time.sleep(1)
                                os.system("cls")

                            dinero_total += dinero
                        
                        vuelto = dinero_total - totalfinal
                        menu_carrito = False
                        menu_ppal = False

                        if cant_m1 + cant_m2 + cant_m3 + cant_m4 + cant_m5 != 0:
                            print("\t    SHIN WHE WENSHA")
                            print("-"*40)
                            print(f"Total Productos: \t\t{cant_m1 + cant_m2 + cant_m3 + cant_m4 + cant_m5}")
                            if cant_m1 != 0:
                                print(f"{cant_m1} Camarón Mandarín \t\t${cant_m1 * 11000}")
                            if cant_m2 != 0:
                                print(f"{cant_m2} Carne Mongoliana \t\t${cant_m2 * 10000}")
                            if cant_m3 != 0:
                                print(f"{cant_m3} Chapsui Pollo \t\t${cant_m3 * 9500}")
                            if cant_m4 != 0:
                                print(f"{cant_m4} Chapsui Carne \t\t${cant_m4 * 12000}")
                            if cant_m5 != 0:
                                print(f"{cant_m5} Parrillada China \t\t${cant_m5 * 15000}")
                            print("-"*40)
                            print(f"Subtotal:\t\t\t${subtotal}")
                            if descuento != 0:
                                print(f"Descuento:\n{descuento}% {nom_desc} \t\t{math.trunc(subtotal*(descuento/100))}")
                            print("-"*40)
                            print(f"Total: \t\t\t\t${math.trunc(totalfinal)}")
                            print("-"*40)
                            print(f"Monto: \t\t\t\t${dinero_total}")
                            print(f"Vuelto: \t\t\t${math.trunc(vuelto)}")
                    else:
                        menu_carrito = False

        else:
            menu_ppal = False