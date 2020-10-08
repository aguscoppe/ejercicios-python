# EJERCICIO 33

n = int(input("Ingrese un número positivo: "))
a = n/2
resultadoAnterior = n

while(resultadoAnterior - a) > 0.0001:
    resultadoAnterior = a
    a = ((n/a) + a) / 2
print("Resultado aproximado:", a)