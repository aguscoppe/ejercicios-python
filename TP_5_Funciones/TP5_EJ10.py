# EJERCICIO 10

def comparar(a, b):
    if a > b:
        return 1
    elif b == a:
        return 0
    return -1
    
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

print(comparar(a, b))