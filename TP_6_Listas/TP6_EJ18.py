import random

def generarSecuencia(cant):
    lista = []
    while cant > 0:
        n = random.randint(1, 20)
        lista.append(n)
        cant -= 1
    return lista

def insertarCeros(lista):
    LIMITE = 20
    nuevaLista = []
    cont = 0
    for i in range(len(lista)):
        cont = cont + lista[i]
        if cont <= 20:
            nuevaLista.append(lista[i])
        else:
            nuevaLista.append(0)
            nuevaLista.append(lista[i])
            cont = lista[i]
    nuevaLista.append(0)
    return nuevaLista
    
n = int(input("Ingresar cantidad de elementos que tendrá la lista: "))

secuencia = generarSecuencia(n)

print(insertarCeros(secuencia))