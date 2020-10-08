# Ejercicio 17-C

tope = int(input("Ingrese un tope: "))
cont = 1
serieC = 1
numMayor = 0

while serieC < tope:

    if serieC > numMayor and serieC <= tope:
        numMayor = serieC

    serieC = cont + serieC
    cont = cont + 1

print(numMayor)