# EJERCICIO 5

def devolverMaximo(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

print(devolverMaximo(a, b))