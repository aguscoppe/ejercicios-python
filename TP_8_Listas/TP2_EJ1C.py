import random

def cargarLista():
    cant = random.randint(10, 99)
    lista = []
    for i in range(cant):
        n = random.randint(1000, 9999)
        lista.append(n)
    return lista

def eliminarElemento(lista, el):
    valorEsta = False
    while el in lista:
        lista.remove(el)
        valorEsta = True
    return valorEsta

# PROGRAMA PRINCIPAL
elem = int(input("Ingrese un número para eliminar de la lista: "))
lista = cargarLista()
#lista.append(2000)
print("Lista:", *lista)
print()

elemEsta = eliminarElemento(lista, elem)
if elemEsta:
    print("Lista sin ", elem, "->", *lista)
else:
    print("El elemento no estaba en la lista")