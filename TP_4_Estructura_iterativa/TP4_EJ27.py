# EJERCICIO 27

n = int(input("Ingrese un número entero: "))
cont = 1

# Conversión de n negativo a positivo
if n < 0:
    n = -n * (-1)

while n != 0:
    n = n // 10
    if n > 0:
        cont = cont + 1

print("El número tiene", cont, "cifra(s)")