# Ejercicio 18-C

tope = int(input("Ingrese un tope: "))
cont = 1
serieC = 1
suma = 0

while serieC < tope:

    if serieC < tope:
        suma = suma + serieC

    serieC = cont + serieC
    cont = cont + 1

print(suma)