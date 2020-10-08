# EJERCICIO 1

def multiplicarNumeros(a, b):
    resultado = 0
    while a > 0:
        resultado = resultado + b
        a = a - 1
    return resultado

print(multiplicarNumeros(3, 5))