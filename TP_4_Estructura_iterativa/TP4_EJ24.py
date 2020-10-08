# EJERCICIO 24

n = int(input("Ingrese un número entero mayor que 0: "))
factorial = 1

if n <= 0:
    print("El número ingresado es inválido")
else:
    while n > 0:
        factorial = factorial * n
        n = n - 1
    print("El factorial es:", factorial)