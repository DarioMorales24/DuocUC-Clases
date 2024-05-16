import os
os.system("cls")

nombre = "Dario Morales Andrades"
vocal = ["A", "E", "I", "O", "U"]
vocales = 0
consonantes = 0

for letra in nombre:
    # print(f"{letra}")
    if letra == " ":
        pass
    else:

        if letra.upper() in vocal:
            vocales += 1
        elif letra.upper() != vocal:
            consonantes += 1


print(f"Cant de Vocales = {vocales}")
print(f"Cant de Consonantes = {consonantes}")