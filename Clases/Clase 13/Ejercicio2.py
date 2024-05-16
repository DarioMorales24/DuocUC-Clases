import os
os.system("cls")

notas = []

for i in range(4):
    os.system("cls")
    nota = float(input(f"Ingrese su nota {i+1}: "))
    notas.append(nota)

notas.sort()
print(notas)