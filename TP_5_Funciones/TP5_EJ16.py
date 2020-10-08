# EJERCICIO 16

def calcularFibonacci(n, b):
    i = 0
    primero = 1
    segundo = 1
    total = 0
    suma = 0

    while primero <= b:
        suma = suma + primero
        i += 1
        total = primero + segundo
        primero = segundo
        segundo = total
    return suma

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

if a > b:
    c = b
    b = a
    a = c

print("Total:", calcularFibonacci(a, b))