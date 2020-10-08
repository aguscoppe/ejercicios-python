# EJERCICIO 12

a = int(input("Ingrese un número entero positivo: "))
b = int(input("Ingrese otro número entero positivo: "))
resultado = 0
aux = b

while aux > 0:
    resultado = resultado + a
    aux = aux - 1

if a < 0 or b < 0:
    print("No ingresaron dos números positivos")
else:
    print("El resultado de", a, "*", b, "es", resultado)