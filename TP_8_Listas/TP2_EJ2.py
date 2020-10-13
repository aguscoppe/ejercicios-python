import random

def generarLista():
    lista = []
    for i in range(50):
        n = random.randint(1, 100)
        lista.append(n)
    return lista

def buscarRepetido(lista):
    hayRepetidos = False
    for i in range(len(lista)):
        cant = lista.count(lista[i])
        if cant > 1:
            hayRepetidos = True
            break
    return hayRepetidos

def devolverUnicos(lista):
    nuevaLista = []
    for i in range(len(lista)):
        cant = lista.count(lista[i])
        if cant == 1:
            nuevaLista.append(lista[i])
    return nuevaLista

# PROGRAMA PRINCIPAL
lista = generarLista()
print("Lista completa:", lista)
print()

if buscarRepetido(lista):
    print("La lista contiene elementos repetidos")
else:
    print("La lista no contiene elementos repetidos")
print()

unicos = devolverUnicos(lista)
if len(unicos) > 0:
    print("Lista con elementos úncios:", unicos)
else:
    print("La lista no tenía elementos únicos")