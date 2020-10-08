# EJERCICIO 4
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese un número entero: "))
if (a % b) == 0:
    print(a, "es múltiplo de", b)
else:
    print(a, "no es múltiplo de", b)
if (b % a) == 0:
    print(b, "es múltiplo de", a)
else:
    print(b, "no es múltiplo de", a)