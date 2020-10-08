# EJERCICIO 15

num = int(input("Ingrese un número: "))
mayor = num
menor = num
cont = 1

while cont < 10:
    if num > mayor:
        mayor = num
    elif num < menor:
        menor = num
    num = int(input("Ingrese un número: "))
    cont = cont + 1

print("El menor número es:", menor)
print("El mayor número es:", mayor)
print("El rango del conjunto es:", mayor - menor)