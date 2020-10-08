# EJERCICIO 20

a = int(input("Ingrese un número entero positivo: "))
b = int(input("Ingrese un número entero positivo menor que el anterior: "))
cont = 0
resultado = a

if a >= b and b != 0:
    while resultado >= b:
        cont = cont + 1
        resultado = resultado - b
    print("Dividendo:", a)
    print("Divisor:", b)
    print("Cociente:", cont)
    print("Resto:", resultado)
else:
    print("Los valores ingreasados son incorrectos")