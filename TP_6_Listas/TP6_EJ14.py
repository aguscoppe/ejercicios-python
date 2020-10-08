import random

def imprimirLista(lista):
    for i in range (len(lista)):
        print(lista[i], end=" ")
    print()

def crearListaAleatoria():
    i = 0
    lista = []
    cant = random.randint(1, 100)
    while i != cant:
        lista.append(random.randint(1, 100))
        i = i + 1
    return lista

def ordenarLista(lista):
    for i in range (len(lista) - 1):
        for j in range (i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    return lista

def busquedaBinaria(dato, lista):
    izq = 0
    der = len(lista) - 1
    indice = -1
    while izq <= der and indice == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            indice = centro
        elif lista[centro] > dato:
            der = centro - 1
        else:
            izq = centro + 1
    return indice

def buscarCoincidencias(a, b):
    print("Primera lista")
    imprimirLista(a)
    print()
    print("Segunda lista")
    imprimirLista(b)
    print()
    i = 0
    listaEliminar = []
    listaNueva = []
    while i != (len(a)):
        indice = busquedaBinaria(a[i], b)
        if indice != -1:
            listaEliminar.append(b[indice])
        else:
            listaNueva.append(a[i])        
        i = i + 1
    print("Lista de eliminación")
    imprimirLista(listaEliminar)
    print()
    print("Lista nueva")
    imprimirLista(listaNueva)

a = ordenarLista(crearListaAleatoria())
b = ordenarLista(crearListaAleatoria())
c = buscarCoincidencias(a, b)