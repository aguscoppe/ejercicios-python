# EJERCICIO 8

def intercambiarValores(a, b):
    c = a
    a = b
    b = c

def calcularMCD(a, b):
    if b > a:
        intercambiarValores(a, b)
    
    resultado = -1
    while resultado != 0:
        resultado = a % b
        a = b
        b = resultado
    return a

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

while a <= 0 or b <= 0:
    print("Los números deben ser mayores que 0")
    a = int(input("Ingrese un número entero: "))
    b = int(input("Ingrese otro número entero: "))

print("El MCD de", a, "y", b, "es:", calcularMCD(a, b))