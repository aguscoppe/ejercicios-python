# EJERCICIO 9

def signo(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

n = int(input("Ingrese un número entero: "))

print(signo(n))