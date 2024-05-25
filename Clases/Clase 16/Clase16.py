import os
os.system("cls")

tablero = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

jugador = "X"

opciones_x = []
opciones_o = []

jugadas_realizadas = []

def mostrar_tablero():
    os.system("cls")
    print("== Gato ==")
    t = ""
    for fila in tablero:
        for num in fila:
            if num in opciones_x:
                t+= f"| X "
            elif num in opciones_o:
                t += f"| O "
            else:
                t += f"| {num} "
        t += "|\n"
    
    print(t)

def opcion_elegida():
    opcion = int(input(f"Jugador {jugador} selecciona: "))

    if opcion < 1 or opcion > 9:
        return False
    
    elif opcion in opciones_x or opcion in opciones_o:
        input("Esta opcion no esta disponible")
        return False

    else:
        if jugador == "X":
            opciones_x.append(opcion)
            jugadas_realizadas.append(opcion)
        else:
            opciones_o.append(opcion)
            jugadas_realizadas.append(opcion)
        return True

def winner():
    win = [
        (1,2,3),(4,5,6),(7,8,9),
        (1,4,7),(2,5,8),(3,6,9),
        (1,5,9),(3,5,7)
    ]
    
    for jugadas in win:
        if all(pos in opciones_x for pos in jugadas):
            input("Gano jugador X")
            break
        if all(pos in opciones_o for pos in jugadas):
            input("Gano jugador O")
            break

def empate():
    jugadas_realizadas.sort()
    if jugadas_realizadas == [1,2,3,4,5,6,7,8,9]:
        input("empate")


ganador = False
while ganador == False:
    winner()
    empate()
    mostrar_tablero()
    if opcion_elegida():
        jugador = "O" if jugador == "X" else "X"
