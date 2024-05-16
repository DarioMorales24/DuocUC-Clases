import os
os.system("cls")

"""lista = []
lista = list()

persona = ["Alan", "Brito", 19, 1.8, False]

print(f"Nombre: {persona[0]}")
print(f"Apellido: {persona[1]}")
print(f"Edad: {persona[2]}")
print(f"Estatura: {persona[3]}")
print(f"Es mujer?: {persona[4]}")


for i in persona:
    print(i)"""

personas = [
    ["Alan", "Brito"],
    ["Pedro", "Pascal"],
    ["María", "Dolores"]
]

apellido = personas[2][0]
print(apellido)

# for persona in personas:
#     for i in persona:
#         print(i)

personas.insert(0,["Holas"])

print(personas)