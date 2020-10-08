# EJERCICIO 7

def calcularFactorial(n):
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1
    return resultado

n = int(input("Ingrese un número entero: "))

print(calcularFactorial(n))