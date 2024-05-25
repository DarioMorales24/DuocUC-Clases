import os
os.system("cls")

tablero =[
    ["A","B","C"],
    ["D","E","F"],
    ["G","H","I"]
]

opciones = []
opciones_x = [] 
opciones_o = []

win = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["A", "D", "G"],
    ["B", "E", "H"],
    ["C", "F", "I"],
    ["A", "E", "I"],
    ["A", "E", "I"],
    ["G", "E", "C"]
]
menu = True

while menu:
    
    
    dibujar_tablero = ""
    os.system("cls")
    for fila in tablero:
        for e in fila:
            opciones.append(e)
            if e in opciones_x:
                dibujar_tablero += (f"| X ")
            elif e in opciones_o:
                dibujar_tablero += (f"| O ")
            else:
                dibujar_tablero += (f"| {e} ")
        dibujar_tablero += "| \n"

    os.system("cls")
    print(dibujar_tablero)
    

    opcion = input("Selecciona una opcion Player X: ").upper()
    opcion2 = input("Selecciona una opcion Player O: ").upper()
    
    if opcion in opciones:
        opciones_x.append(opcion)
    if opcion2 in opciones:
        opciones_o.append(opcion2)
    os.system("cls")

    opciones_o.sort()
    opciones_x.sort()
    if opciones_x in win:
        print("You win player X")
        menu = False
    elif opciones_o in win:
        print("You win player O")
        menu = False

