import os
os.system("cls")

numero = 31

if numero > 1:
    for i in range(2,numero):
        if (numero % i) == 0 :
            print(numero, " No es un numero primo")
            break
        else:
            print(numero, " Es un numero primo")
else:
    print(numero, "no es un numero menor que 1") 

lim = 20
num = 2

while num < 20:
    esPrimo = True
    divisor=2
    while esPrimo:
    
