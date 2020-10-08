# EJERCICIO 26

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
copia = a

if a > b:
    a = b
    b = copia
    copia = a

resultado = 0

while a < (b - 1):
    a = a + 1
    resultado = resultado + a

print("Las sumas de los números entre", copia, "y", b, "dan como resultado:", resultado)