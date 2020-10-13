import random

def cargarLista():
    cant = random.randint(10, 99)
    lista = []
    for i in range(cant):
        n = random.randint(1000, 9999)
        lista.append(n)
    return lista

# PROGRAMA PRINCIPAL
lista = cargarLista()
print("Lista:", *lista)