"""
print("Hola") #<- comando de salida
nombre = input("Ingrese su nombre ") #<- comando de entrada
print(f"pero el profesor {nombre} nos dió otra oportunidad") # comando de salida concatenado

"""

"""
# ---------------------------------------------------------------------------------------------------
#                                            VALIDACIONES
#----------------------------------------------------------------------------------------------------

edad = int(input("Ingrese su edad: "))

if edad == 0 and edad < 1 :
    print("Ud nació")
elif edad < 18:
    print("UD es menor de edad")
elif edad >= 18 :
    print("Ud es mayor de edad")
else:
    print("No ha nacido")

# esto es un sistema de validacion if, elif, else

"""


"""
"""

# MENU SIMPLE!!!!!!

print("===BEBIDAS===")
print("1) Cocacola")
print("2) Pepsi")
print("3) Fanta")
opcion = int(input("Escoja una opcion: "))


if opcion == 1:
    print("Ud eligió Cocacola")
elif opcion == 2:
    print("Ud eligió Pepsi")
elif opcion == 3:
    print("Ud eligió la Fanta")
else:
    print("Opcion no es valida")

