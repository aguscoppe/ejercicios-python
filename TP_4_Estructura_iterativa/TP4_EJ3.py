# EJERCICIO 3

num = int(input("Ingrese un número o -1 para finalizar: "))
limite = 1000
while num != -1:
    limite = limite - 1
    num = int(input("Ingrese un número o -1 para finalizar: "))

if(limite % 2 == 0):
    print("La cantidad de números es par")
else:
    print("La cantidad de números es impar")