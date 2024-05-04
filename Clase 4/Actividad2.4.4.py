import os, time
os.system("cls")

numero = int(input("Ingrese el numero de boletos que desea vender: "))
totalIngreso = 0

for i in range(numero):
    precio = int(input(f"Ingrese el precio delo boleto numero {i+1}: "))
    if type(precio) == int:
        totalIngreso += precio
    else:
        print("Ingrese un valor numerico")
        time.sleep(2)
        os.system("cls")

print(f"Ud a generado ${totalIngreso} con la venta de los boletos")