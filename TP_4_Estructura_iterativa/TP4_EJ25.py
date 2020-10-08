# EJERCICIO 25

a = int(input("Ingrese un número natural: "))
b = int(input("Ingrese otro número natural: "))
cont = 1
resultado = a

while(cont < b and b != 0):
    resultado = resultado * a
    cont = cont + 1

if b == 0:
    resultado = 1

if b < 0:
    print("Error: el segundo número no puede ser negativo")
else:
    print(a, "elevado a", b, "es igual a", resultado)