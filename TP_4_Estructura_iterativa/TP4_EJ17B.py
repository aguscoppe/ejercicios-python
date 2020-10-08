# Ejercicio 17-B

tope = int(input("Ingrese un tope: "))
serieB = 0
auxB = 1
numMayor = 0

while serieB < tope:
    serieB = auxB*(-1)**auxB

    if serieB > numMayor and serieB <= tope:
        numMayor = serieB

    auxB = auxB + 1

print(numMayor)