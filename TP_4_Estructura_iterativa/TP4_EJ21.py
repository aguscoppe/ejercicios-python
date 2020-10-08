# EJERCICIO 21

n = int(input("Ingrese un número natural: "))

while n > 2:
    if n % 2 != 0:
        n = n - 1
        print(n)
    else:
        n = n - 2
        print(n)