# EJERCICIO 6

num = int(input("Ingrese un número o -1 para finalizar: "))
cantPares = 0
cantImpares = 0

while num != -1:
    if num % 2 == 0:
        cantPares = cantPares + 1
    else:
        cantImpares = cantImpares + 1
    num = int(input("Ingrese un número o -1 para finalizar: "))

print() # agregar salto de linea

if cantPares < 1 and cantImpares < 1:
    print("No se ingresaron números")
else:
    print("Cantidad de elementos impares:", cantImpares)
    print("Cantidad de elementos pares:", cantPares)