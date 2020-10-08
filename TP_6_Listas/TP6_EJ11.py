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
def detectarPosicion(n, lista):
    asc = verificarAscendente(lista)
    minimo = -1
    maximo = -1
    resultado = 1
    i = 0
    while resultado >= 0 and i <= (len(lista) - 1):
        if asc == True:
            resultado = n - lista[i]
            minimo = i
        else:
            resultado = lista[i] - n
            maximo = i
        i = i + 1
    if minimo != -1:
        return minimo
    else:
        return maximo

# agrega el valor de n en el índice pos de la lista
def agregarElemento(lista, pos, n):
    nuevaLista = []
    for i in range (len(lista)):
        if i == pos:
            nuevaLista.append(n)
        nuevaLista.append(lista[i])
    return nuevaLista
    
n = int(input("Ingrese el número que quiere insertar en la lista (0 - 100): "))

a = crearLista()

a = ordenarLista(a)

pos = detectarPosicion(n, a)

print()
print("Lista anterior:", a)
print()
print("Número a insertar:", n)
print()
print("Lista nueva:", agregarElemento(a, pos, n))