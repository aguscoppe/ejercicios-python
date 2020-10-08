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

def buscarDato(dato):
    lista = crearLista()
    indice = -1
    for i in range (len(lista)):
        if lista[i] == dato:
            indice = i
    return indice

n = int(input("Ingrese el dato que quiere buscar en la lista: "))

i = buscarDato(n)

if i == -1:
    print("El número no está en la lista")
else:
    print("El número", n, "está en el índice:", i)