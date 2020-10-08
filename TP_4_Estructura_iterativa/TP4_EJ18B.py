# Ejercicio 18-B

tope = int(input("Ingrese un tope: "))
serieB = 0
auxB = 1
suma = 0

while serieB < tope:
    serieB = auxB*(-1)**auxB
    auxB = auxB + 1
    
    if serieB <= tope:
        suma = suma + serieB

print(suma)