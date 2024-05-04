nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))

prom = round((nota1 + nota2 + nota3)/3, 1)

if prom >= 4:
    print(f"Ud ha sido aprobado y su promedio es de {prom}")
elif prom < 4 and prom > 0 :
    print (f"Ud ha sido reprobado y su promedio es de {prom}")
else:
    print("Ingrese notas validas porfavor")
