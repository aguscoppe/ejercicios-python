def devolverMayor(lista):
    mayor = -1
    cont = 0
    for i in range (len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        elif lista[i] == mayor:
            cont += 1
    if cont > 0:
        return -1
    return mayor

def ingresarDatos():
    lista = []
    for i in range(3):
        n = int(input("Ingrese un número positivo: "))
        while n < 0:
            print("El número debe ser positivo")
            n = int(input("Ingrese un número positivo: "))
        lista.append(n)
    mayor = devolverMayor(lista)
    if mayor == -1:
        print("No existe mayor estricto")
    else:
        print("El mayor estricto es:", mayor)

ingresarDatos()