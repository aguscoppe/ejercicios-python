# EJERCICIO 7

num = int(input("Ingrese un número o -1 para finalizar: "))
menor = num
mayor = num
while num != -1:
    if num > mayor:
        mayor = num
    elif num < menor:
        menor = num
    num = int(input("Ingrese un número o -1 para finalizar: "))

print() # salto de línea

if menor == -1 and mayor == -1:
    print("No se ingresaron números")
else:
    print("El mayor número ingresado fue:", mayor)
    print("El menor número ingresado fue:", menor)