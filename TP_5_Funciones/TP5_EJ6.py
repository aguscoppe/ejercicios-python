# EJERCICIO 6

def esMultiplo(a, b):
    resultado = 0
    i = 0
    while resultado < a:
        i = i + 1
        resultado = b * i
    if resultado == a:
        return True
    else:
        return False

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

print(esMultiplo(a, b))