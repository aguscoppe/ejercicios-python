#EJERCICIO 10
l1 = int(input("Ingrese un lado del triángulo: ")) #el nombre de las variables empieza con L minúscula, no con 1 (uno)
l2 = int(input("Ingrese otro lado del triángulo: "))
l3 = int(input("Ingrese el último lado del triángulo: "))
a = 0
b = 0
c = 0
suma = 0
sumaCuadrada = 0

if l1 > l2 and l1 > l3:
    a = l1
    b = l2
    c = l3
elif l2 > l1 and l2 > l3:
    a = l2
    b = l1
    c = l3
else:
    a = l3
    b = l1
    c = l2

suma = b + c
sumaCuadrada = b**2 + c**2

if a >= suma:
    print("No se trata de un triángulo")
elif (a**2) == sumaCuadrada:
    print("Se trata de un triángulo rectángulo")
elif (a**2) > sumaCuadrada:
    print("Se trata de un triángulo obtusángulo")
elif (a**2) < sumaCuadrada:
    print("Se trata de un triángulo acutángulo")