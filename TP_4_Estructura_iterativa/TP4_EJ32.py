# EJERCICIO 32

n = int(input("Ingrese un número entero: "))
i = 0
primero = 1
segundo = 1
total = 0
suma = 0

while i < n:
    print(primero)
    suma = suma + primero
    i += 1
    total = primero + segundo
    primero = segundo
    segundo = total

print("Total:", suma)