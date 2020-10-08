# EJERCICIO 12

def extraerNumero(n, dig):
    digito = 0
    while dig >= 0 and n != 0:
        digito = n % 10
        n = n // 10
        dig = dig - 1
    if n == 0 and dig > 0:
        return -1
    else:
        return digito

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese qué digito quiere extraer: "))

if a < 0:
    a = -a
if b < 0:
    b = -b

print(extraerNumero(a, b))