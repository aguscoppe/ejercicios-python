# EJERCICIO 4

def esPar(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Ingrese un número: "))

print(esPar(n))