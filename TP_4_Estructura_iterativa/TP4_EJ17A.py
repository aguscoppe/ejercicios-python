# Ejercicio 17-A

tope = int(input("Ingrese un tope: "))
serieA = 0
auxA = 0
num = 3
numMayor = 0

while serieA < tope:
    if num == 3:
        num = num - 1
    else:
        num = num + 1
    serieA = num**auxA
    
    if num % 2 != 0:
        auxA = auxA + 1
    
    if serieA > numMayor and serieA <= tope:
        numMayor = serieA

print(numMayor)