# EJERCICIO 13

num = int(input("Ingrese un número: "))
menor = num
cont = 1
orden = cont

while cont <= 10:
    if num < menor:
        menor = num
        orden = cont
    num = int(input("Ingrese otro número: "))
    cont = cont + 1

print("El número de menor valor ingresado fue:", menor)
print("Fue el número en posición", orden)