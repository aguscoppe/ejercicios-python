# EJERCICIO 11

import random

def crearLista():
    n = random.randint(1, 100)
    lista = []
    for i in range (n):
        num = random.randint(1, 100)
        lista.append(num)
    return lista

def ordenarLista(lista):
    for i in range (len(lista) - 1):
        for j in range (i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    return lista

# devuelve True si la lista es ascendente
# o False si la lista no es ascendente
def verificarAscendente(lista):
    valor = lista[0]
    i = 0
    asc = False
    while valor == lista[i]:
        i = i + 1
        if valor < lista[i]:
            asc = True
    return asc

# devuelve la posición donde el número será insertado
def agregarElemento(n, lista):
    asc = verificarAscendente(lista)
    i = 0
    if asc == True:

n = int(input("Ingrese el número que quiere insertar en la lista (0 - 100): "))

a = crearLista()

a = ordenarLista(a)

print()
print("Lista anterior:", a)
print()
print("Número a insertar:", n)
print()
print("Lista nueva:", agregarElemento(a, n))