import random

def crearLista():
    n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    lista = []
    while n != -1:
        lista.append(n)
        n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    return lista

def esCapicua(lista):
    i = 0
    j = len(lista) - 1
    esCapicua = True
    while i < j:
        if lista[i] != lista[j]:
            esCapicua = False
            break
        i += 1
        j -= 1
    return esCapicua

# PROGRAMA PRINCIPAL
lista = crearLista()
if esCapicua(lista):
    print("La lista es capicúa")
else:
    print("La lista no es capicúa")