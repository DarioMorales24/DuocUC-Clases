from os import system as hola
hola("cls")

# Crea una clave con los 2 primeros digitos del primer nombre en mayusculas
# los 3 ultimos digitos del apellido paterno en minusculas
# mas la cantidad de caracteres totales del apellido materno

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su primer apellido: ")
apellido2 = input ("Ingrese su segundo apellido: ")
contrasena = ""

# contraseña.append(nombre.upper()[:2])
contrasena += nombre.upper()[:2]
contrasena += apellido.lower()[-3:]
contrasena += str(len(apellido2))
print(contrasena)