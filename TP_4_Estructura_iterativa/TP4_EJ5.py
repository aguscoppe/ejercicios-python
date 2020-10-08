# EJERCICIO 5

num = int(input("Ingrese un número o -1 para finalizar: "))
cont = 0
mayor = num

while num != -1: 
    if(num > mayor):
        cont = 0
        mayor = num
    num = int(input("Ingrese un número o -1 para finalizar: "))
    if num != -1:
        cont = cont + 1

if(mayor == -1):
    print("No se ingresó ningún número")
else:
    print("Hubo", cont, "valores menores que", mayor)