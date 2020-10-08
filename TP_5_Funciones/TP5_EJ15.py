# EJERCICIO 15

def concatenarNumeros(a, b):
    digito = 0
    total = 0
    multi = 1
    while b != 0:
        digito = b % 10
        b = b // 10
        total = total + digito * multi
        multi = multi * 10
        if b == 0:
            b = a
            a = 0
    return total

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

if a < 0:
    a = -a

print(concatenarNumeros(a, b))