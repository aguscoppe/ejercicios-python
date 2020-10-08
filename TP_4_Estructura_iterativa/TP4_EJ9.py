# EJERCICIO 9

num = int(input("Ingrese un número: "))
total = num # acumulador
cont = 1 # contador
while cont < 100:
    num = int(input("Ingrese otro número: "))
    total = total + num
    cont = cont + 1
promedio = total / cont
print("El promedio es:", promedio)