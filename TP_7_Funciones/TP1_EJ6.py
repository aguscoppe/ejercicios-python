def calcularCifras(n):
    cifras = 0
    while n > 0:
        cifras += 1
        n = n // 10
    return cifras

def concatenarNumeros(a, b):
    cifras = calcularCifras(b)
    total = a * (10**cifras)
    total += b
    return total

n1 = int(input("Ingrese un número entero positivo: "))
n2 = int(input("Ingrese otro número entero positivo: "))
print(concatenarNumeros(n1, n2))