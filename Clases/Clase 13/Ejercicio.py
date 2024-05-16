import os
os.system("cls")

listado_trabajadores = []

menu = True

for i in range(3):
    os.system("cls")
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el Apellido: ")
    edad = input("Ingresa la edad: ")

    trabajador = [nombre, apellido, edad]
    listado_trabajadores.append(trabajador)

print(listado_trabajadores)
