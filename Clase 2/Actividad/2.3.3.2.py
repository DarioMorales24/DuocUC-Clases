user = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

if user == "pedro":
    if password == "1234":
        print("Bienvenido sr.Pedro")
    else:
        print("Tu contraseña es incorrecta")
elif user == "angel":
    if password == "a4s1":
        print("Bienvenido sr.Angel")
    else:
        print("Tu contraseña es incorrecta")
else:
    print("Este usuario no existe")