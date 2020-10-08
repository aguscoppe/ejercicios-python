# EJERCICIO 13

def devolverDigitos(n, digitos):
    dig = 0
    resultado = 0
    copia = n
    multi = 1
    while digitos != 0:
        dig = n % 10
        n = n // 10
        resultado = resultado + dig * multi
        multi = multi * 10
        digitos = digitos - 1
        if resultado == copia:
            digitos = 0
    return resultado

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese la cantidad de dígitos a extraer: "))

print(devolverDigitos(a, b))