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

# devuelve True si la lista es ascendiente
# y devuelve False si la lista es descendiente
def verificarAsc(lista):
    fin = False
    asc = False
    i = 0
    while fin == False:
        if lista[i] < lista[i + 1]:
            asc = True
            fin = True
        elif lista[i] > lista[i + 1]:
            asc = False
            fin = True
        else:
            i = i + 1
    return asc

def insertarNumero(lista, n):
    asc = verificarAsc(lista)
    if asc == True:
        nuevaLista = []
        for i in range(len(lista)):
            if n - lista[i] <= 0:
                nuevaLista[i-1].append(n)
            nuevaLista.append(lista[i])
            i = i + 1
        return nuevaLista

n = int(input("Ingrese el número que quiere insertar en la lista: "))

a = crearLista()

a = ordenarLista(a)

print(insertarNumero(a, n))