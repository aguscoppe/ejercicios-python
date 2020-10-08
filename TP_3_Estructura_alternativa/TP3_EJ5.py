# EJERCICIO 5
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))
if (base > 0) and (altura > 0):
    sup = (base * altura) / 2
    print("La superficie del triángulo es de: ", sup)
else:
    print("Error en el ingreso de datos")