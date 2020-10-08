# EJERCICIO 23

m = int(input("Ingrese un número natural: "))
suma = 0
cont = 0
aux = m
multi = 1

while cont < m:
    suma = suma + aux
    aux = aux - 1
    cont = cont + 1

aux = m

while aux < (m*2):
    multi = multi * aux
    aux = aux + 1

print(suma)
print(multi)