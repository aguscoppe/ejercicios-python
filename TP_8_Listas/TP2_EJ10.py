import random

def crearLista():
    lista = []
    for i in range(100):
        lista.append(random.randint(0, 100))
    return lista

lista = crearLista()
impares = [i for i in range(len(lista)) if i % 2 != 0]

print("Lista original:", *lista)
print("Números impares:", *impares)