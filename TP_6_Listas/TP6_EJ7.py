def crearLista():
    n = int(input("Ingrese un número entre 1 y 20 o -1 para finalizar: "))
    MENOR = 1
    MAYOR = 20
    lista = []    
    while n != -1:
        if n < MENOR or n > MAYOR:
            print("El número está fuera de rango")
        else:
            lista.append(n)
        n = int(input("Ingrese un número entre 1 y 20 o -1 para finalizar: "))            
    return lista

def ordenarLista():
    lista = crearLista()
    for i in range (len(lista) - 1):
        for j in range(i + 1, (len(lista))):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    return lista
    
def busquedaBinaria(dato):
    lista = ordenarLista()
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

n = int(input("Ingrese el dato que quiere buscar en la lista: "))

i = busquedaBinaria(n)

if i == -1:
    print("El número no está en la lista")
else:
    print("El número", n, "está en el índice:", i)