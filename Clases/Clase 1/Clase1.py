# Hola mundo

print("Hola Mundo!")

#Agregar Variables 

# OJO!!!!! LAS VARIABLES SIEMPRE EN MINUSCULAS

nombre = input("Ingrese su nombre: ") # <- nombre es donde se guarda la variable en la cual se intruduce el valor del input
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingrese su edad: ")) # <- int es una opcion que asegura q lo que este a dentro sea un integer(entero)
print("Hola", nombre, apellido)
print(f"Hola {nombre}, tu tienes {edad} años") # <- esta es otra manera de usar print, esta es mas recomendada
print(f"Hola {nombre} {apellido}, tu tienes {edad} años")

#---------------------------------------------------------------------------------------------------------------------

print(f"Nombre: \t {nombre}")
print(f"Apellido: \t {apellido}")
print(f"Edad: \t\t {edad}")

# ctrl k + c  <- comenta una linea 
# ctrl k + u <- descomenta una linea



