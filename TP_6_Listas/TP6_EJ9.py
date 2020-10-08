import random

def crearListaEnteros(n):
    lista = []
    for i in range (n):
        n = random.randint(1, 20)
        lista.append(n)
    return lista

def crearListaBooleanos(lista):
    nuevaLista = []
    i = 0
    while i < (len(lista) - 1):
        if lista[i] <= lista[i + 1]:
            nuevaLista.append(True)
        else:
            nuevaLista.append(False)
        i = i + 1
    return nuevaLista

n = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))

lista = crearListaEnteros(n)

print(lista)

print(crearListaBooleanos(lista))