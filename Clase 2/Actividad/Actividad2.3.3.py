edad = int(input("Ingrese su edad: "))

if edad < 18 and edad > 0 :
    print("Ud es menor de edad")
elif edad >= 18:
    print("Ud es mayor de edad")
else:
    print("Ingrese una edad valida")