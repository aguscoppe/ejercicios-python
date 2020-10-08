# EJERCICIO 11

def calcularRaiz(n):
    a = n/2
    resultadoAnterior = n
    
    while(resultadoAnterior - a) > 0.0001:
        resultadoAnterior = a
        a = ((n/a) + a) / 2
    return a

n = int(input("Ingrese un número positivo: "))

if n < 0:
    print("El número debe ser positivo")
else:
    print("Resultado aproximado:", calcularRaiz(n))