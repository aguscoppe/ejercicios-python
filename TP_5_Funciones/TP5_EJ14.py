# EJERCICIO 14

def devolverDigitoCentral(n):
    copia = n
    digitoActual = 0
    digitoCentral = 0
    totalDigitos = 0
    
    if n % 2 == 0:
        return -1

    while n > 0:
        digitoActual = n % 10
        n = n // 10
        totalDigitos = totalDigitos + 1
        if n == 0 and totalDigitos % 2 != 0:
            digitoCentral = totalDigitos // 2 + 1
            totalDigitos = 0
    
    while totalDigitos != digitoCentral:
        digitoActual = copia % 10
        copia = copia // 10
        totalDigitos = totalDigitos + 1

    return digitoActual

n = int(input("Ingrese un número entero: "))

print("El dígito central es:", devolverDigitoCentral(n))