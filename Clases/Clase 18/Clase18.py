import os
os.system("cls")

def menu_ppal():
    print("=== Menú Cine ===")
    print("1. Comprar Entradas")
    print("2. Cancelar Entradas")
    print("3. Visualizar Sala")
    print("4. Listar Ventas")

def seleccion_ppal(max_opcion):
    opcion = 0
    elegir = True
    while elegir:
        try:
            opcion = int(input("Ingrese una de las opciones: "))
        except:
            print("Opcion no disponible, intente nuevamente")
        
        if opcion < 1 or opcion > max_opcion:
            input("Opcion no disponible, presione enter para continuar")

        else:
            return opcion

sala = [
    ["A1","A2","A3","A4"],
    ["B1","B2","B3","B4"],
    ["C1","C2","C3","C4"],
    ["D1","D2","D3","D4"],
]

todos_los_asientos = []
asientos_ocupados = []
asientos_comprados = []

def dibujar_sala():
    dibujo = "\n== Sala 1 ==\n"
    for fila in sala:
        for asiento in fila:
            todos_los_asientos.append(asiento)
            dibujo += f"| {asiento} "
        dibujo += f"|\n"

    print(dibujo)

def comprar_entrada():
    entrada = input("Seleccione una de las entradas disponibles: ").upper()
    if entrada in todos_los_asientos and entrada not in asientos_ocupados:
        print("Asiento disponible")
        asientos_ocupados.append(entrada)
    else:
        print("Asiento no disponible")


salir = False
while salir == False:
    os.system("cls")
    menu_ppal()
    
    opcion = seleccion_ppal(4)
    if opcion == 1:
        print("== Comprar Entradas ==")
        dibujar_sala()
        comprar_entrada()
    elif opcion == 2:
        print("== Cancelar Entradas ==")
    elif opcion == 3:
        print("== Visualizar Sala ==")
        dibujar_sala()
    elif opcion == 4:
        print("== Listar Ventas ==")

    input("Presione enter para continuar")