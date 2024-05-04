import os, time
os.system("cls")

choice = True
deuda = 100000
reg = 1
while reg == 1:
    while choice == 1:
        print("== Menú ==")
        print("1. Comprar")
        print("2. Pagar Deuda Total")
        print("3. Abonar Deuda")
        print("4. Imprimir Boleta")
        opcion = 0
        eleccion = 0

        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 3:
                print("Ingrese una opcion valida")
                time.sleep(1)
                os.system("cls")
            else:
                choice = 2
        except:
            print("Ingrese un valor numerico")
            time.sleep(1)
            os.system("cls")    

    if opcion == 1:
        print("Aun no puedes comprar")
        time.sleep(1)    

        try: 
            print("Que deseas hacer: ")
            print("1. Regresar al menu principal")
            print("2. Finalizar sesion")
            eleccion = int(input("Selecciona una opcion: "))
            if eleccion == 1:
                reg = 1
                choice = 1
                os.system("cls")
            elif eleccion == 2:
                print("Adios")
        except:
            print("Ingrese un valor numerico")
            time.sleep(1)
            os.system("cls")

    elif opcion == 2:
        dinero = 0
        dineroTotal = 0
            
        print(f"Ud debe cancelar ${deuda}")
        while dineroTotal < deuda or dineroTotal > deuda:
            try:
                dinero = int(input("Ingrese un monto: $"))
                dineroTotal += dinero
                if dineroTotal < deuda:
                    print(f"Ud debe cancelar ${deuda-dineroTotal}")
                elif dineroTotal > deuda:
                    print("Ud no puede ingresar un monto mayor a su deuda")
                    print("Vuelva a comenzar")
                    dineroTotal = 0
                    time.sleep(1)
                    os.system("cls")
                elif dineroTotal == deuda:
                    
                    print("Ud ya no tiene deuda con nosotros")
                    print("Gracias por contar con nosotros")
                else:
                    print("Error")
            except dinero < 0 or ValueError:
                print("Ingrese un monto válido")

                try: 
                    print("Que deseas hacer: ")
                    print("1. Regresar al menu principal")
                    print("2. Finalizar sesion")
                    eleccion = int(input("Selecciona una opcion: "))
                    if eleccion == 1:
                        reg = 1
                        choice = 1
                        os.system("cls")
                    elif eleccion == 2:
                        print("Adios")
                except:
                    print("Ingrese un valor numerico")
                    time.sleep(1)
                    os.system("cls")
    elif opcion == 3:
        dinero = 0
        dineroTotal = 0
        deuda = deuda
            
        print(f"Ud debe cancelar ${deuda}")
        try:
            dinero = int(input("Ingrese un monto: "))
            dineroTotal += dinero
            if dineroTotal < deuda:
                print(f"Ud debe cancelar ${deuda-dineroTotal}")
                deuda = deuda - dineroTotal
            elif dineroTotal > deuda:
                print("Ud no puede ingresar un monto mayor a su deuda")
                print("Vuelva a comenzar")
                dineroTotal = 0
                time.sleep(1)
                os.system("cls")
            else:
                print("Ud ya no tiene deuda con nosotros")
                print("Gracias por contar con nosotros")
        except dinero < 0 or ValueError:
            print("Ingrese un monto válido")

            try: 
                print("Que deseas hacer: ")
                print("1. Regresar al menu principal")
                print("2. Finalizar sesion")
                eleccion = int(input("Selecciona una opcion: "))
                if eleccion == 1:
                    reg = 1
                    choice = 1
                    os.system("cls")
                elif eleccion == 2:
                    print("Adios")
            except:
                print("Ingrese un valor numerico")
                time.sleep(1)
                os.system("cls")

