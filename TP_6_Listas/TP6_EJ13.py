def crearLista():
    n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    lista = []
    while n != -1:
        lista.append(n)
        n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))  
    return lista

def revisarLista(lista):
    largo = len(lista)
    asc = 0
    desc = 0
    iguales = 0
    for i in range (largo - 1):
        if lista[i] < lista[i + 1]:
            asc = asc + 1
        elif lista[i] > lista[i + 1]:
            desc = desc + 1
        elif lista[i] == lista[i + 1]:
            iguales = iguales + 1
    if largo == 0:
        print("La lista está vacía")
    elif asc == (largo - 1):
        print("La lista está en orden ascendente")
    elif desc == (largo - 1):
        print("La lista está en orden descendente")
    elif iguales == (largo - 1):
        print("Todos los elementos de la lista son iguales")
    else:
        print("La lista está desordenada")
           
lista = crearLista()

revisarLista(lista)