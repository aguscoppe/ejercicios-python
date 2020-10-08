# Ejercicio 16-A

cont = 0
serieA = 0
auxA = 0
num = 3

while cont < 20:
    
    if num == 3:
        num = num - 1
    else:
        num = num + 1
    serieA = num**auxA
    print(serieA)
    
    if num % 2 != 0:
        auxA = auxA + 1
    
    cont = cont + 1