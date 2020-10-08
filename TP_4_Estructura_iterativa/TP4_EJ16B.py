# Ejercicio 16-B

cont = 0
serieB = 0
auxB = 1

while cont < 20:
    serieB = auxB*(-1)**auxB
    print(serieB)
    auxB = auxB + 1
    cont = cont + 1