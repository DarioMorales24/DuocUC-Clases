import os
os.system("cls")

print("¿Cuál de los siguientes animales vive en el mar?")
print("Perro")
print("Cocodrilo")
print("Conejo")
print("Tiburón")
resp = input()
puntaje = 0

if resp == "Cocodrilo":
    puntaje = puntaje + 0.5
elif resp == "Tiburón":
    puntaje = puntaje + 1
else:
    puntaje = puntaje

print(f"Su puntaje es {puntaje}")