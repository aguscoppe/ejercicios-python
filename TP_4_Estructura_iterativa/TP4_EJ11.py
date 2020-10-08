# EJERCICIO 11

num = int(input("Ingrese un número entero: "))
limite = 1
mayor = num

while limite < 10:
    num = int(input("Ingrese otro entero: "))
    limite = limite + 1
    if num > mayor:
        mayor = num

print("El mayor número ingresado fue:", mayor)