# EJERCICIO 2

num = int(input("Ingrese un número o -1 para finalizar: "))
primero = num
while num != -1:
    ultimo = num
    num = int(input("Ingrese un número o -1 para finalizar: "))
if primero == -1:
    print("No se ingresaron números")
else:
    print("El primer número fue:", primero)
    print("El último número fue:", ultimo)