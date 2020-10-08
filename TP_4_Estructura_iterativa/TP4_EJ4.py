# EJERCICIO 4

num = int(input("Ingrese un número o -1 para finalizar: "))
cont = 0
posPar = 0

while num != -1:
    cont = cont + 1
    if cont % 2 == 0 and num != -1:
        posPar = num
    num = int(input("Ingrese un número o -1 para finalizar: "))

if(cont >= 2):
    print("El último número en posición par fue:", posPar)
else:
    print("Ningún número estuvo en una posición par")