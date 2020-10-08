import random

def crearLista():
    lista = []
    n = random.randint(1, 99)
    while n != 0:
        lista.append(n)
        n = random.randint(0, 99)
    return lista

def leerLista(lista):
    for i in range (len(lista)):
        print(lista[i], end=" ")

def imprimirMinimo(lista):
    valorMin = lista[0]
    pos = []
    for i in range(len(lista)):
        if lista[i] < valorMin:
            valorMin = lista[i]
    for j in range(len(lista)):
        if lista[j] == valorMin:
            pos.append(j)

    print("Lista completa:")
    leerLista(lista)
    print()
    print("El valor mínimo es", valorMin)
    print("El valor está en la(s) posicion(es):")
    leerLista(pos)

lista = crearLista()

imprimirMinimo(lista)