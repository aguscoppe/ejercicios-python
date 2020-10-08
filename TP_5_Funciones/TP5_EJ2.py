# EJERCICIO 2

def multiplicarNumeros(a, b):
    resultado = 0
    while a > 0:
        resultado = resultado + b
        a = a - 1
    return resultado

def potenciaNumeros(a, b):
    resultado = 1
    while b > 0:
        resultado = resultado * multiplicarNumeros(a, 1)
        b = b - 1
    return resultado

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

print(a, "elevado a la", b, "es:", potenciaNumeros(a, b))