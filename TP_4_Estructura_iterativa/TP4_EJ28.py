# EJERCICIO 28

n = int(input("Ingrese un número entero: "))
ultimo = 0
aux = 0
copia = n

if copia < 0:
    n = n * (-1)

while(n != 0):  
    ultimo = n % 10
    n = n // 10
    if n != 0:
        aux = (aux + ultimo) * 10
    else:
        aux = aux + ultimo

if copia < 0:
    aux = aux * (-1)

print("Al invertir", copia, "obtenemos", aux)