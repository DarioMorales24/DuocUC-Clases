print("¿Cual es la mitica frase de vegeta? (4 pts)")
print("1) Ven y sana mi dolor")
print("2) Sexoooo")
print("3) Su nivel de pelea es de mas de 9000")
print("4) Gokú sin duda eres el dragon ball z")
resp1 = int(input())

print("¿Cual es la mitica frase de Gokú? (4  pts)")
print("1) Ya basta freezer")
print("2) Que buena rola vegeta")
print("3) Eres una basura vegeta")
print("4) vegeta sin duda eres el principe de los namekianos")
resp2 = int(input())

print("¿Cual es la bola del dragon que tiene gokú? (6 pts)")
print("1) 1 estrella")
print("2) 3 estrellas")
print("3) 7 estrellas")
print("4) 4 estrellas")
resp3 = int(input())
puntaje = 0

if resp1 == 1:
    puntaje = puntaje
elif resp1 == 2 :
    puntaje = puntaje
elif resp1 == 3:
    puntaje = puntaje + 4
elif resp1 == 4:
    puntaje = puntaje
else:
    print("Selecciona una opcion valida insecto") 

if resp2 == 1:
    puntaje = puntaje + 4
elif resp2 ==2 :
    puntaje = puntaje
elif resp2 == 3:
    puntaje == puntaje
elif resp2 == 4:
    puntaje = puntaje
else:
    print("Selecciona una opcion valida insecto") 

if resp3 == 1:
    puntaje = puntaje
elif resp3 == 2 :
    puntaje = puntaje
elif resp3 == 3:
    puntaje == puntaje
elif resp3 == 4:
    puntaje = puntaje + 6
else:
    print("Selecciona una opcion valida insecto") 

print(f"Tu puntaje final es de: {puntaje}")
print(f"Y tu nota es: {round(puntaje / 2,1)}")