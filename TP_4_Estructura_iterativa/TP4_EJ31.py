# EJERCICIO 31

h = int(input("Ingrese un número natural: "))
# el valor inicial de i es 2 ya que es innecesario verificar si
# obtenemos 0 como resto al dividirlo por 1
i = 2 
cont = 0

# no utilizamos <= porque verificar
# si el n es divisible por si mismo es innecesario
while(i < h):
    if h % i == 0:
        cont += 1
    i += 1

if cont > 0:
    print("El número no es primo")
else:
    print("El número es primo")