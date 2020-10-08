def leerLista():
    n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    lista = []
    while n != -1:
        lista.append(n)
        n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    return lista

def calcularProducto(lista):
    producto = 1
    sumaImpares = 0
    for i in range (len(lista)):
        if i % 2 == 0:
            producto = producto * lista[i]
        else:
            sumaImpares = sumaImpares + lista[i]
    print()
    print("Lista leída:", lista)
    if sumaImpares == 0:
        print("Error: no puede realizarse la división")
    else:
        print("Producto de pares dividido por suma de impares:", producto / sumaImpares)

def sumarExtremos(lista):
    i = 0
    j = len(lista) - 1
    nuevaLista = []
    while i <= j:
        if lista[i] != lista[j]:
            suma = lista[i] + lista[j]
        else:
            suma = lista[i]
        nuevaLista.append(suma)
        j = j - 1
        i = i + 1
    print("Nueva lista con las sumas de los números en extremos opuestos:", nuevaLista)

def compararLaterales(lista):
    nuevaLista = []
    for i in range (len(lista)):
        if (i + 1) >= len(lista):
            if lista[i] == lista[i - 1] and lista[i] == lista[0]:
                nuevaLista.append(lista[i])
        else:
            if lista[i] == lista[i - 1] and lista[i] == lista[i + 1]:
                nuevaLista.append(lista[i])               
    print("Lista con elementos laterales iguales:", nuevaLista)
            
v = leerLista()

calcularProducto(v)

sumarExtremos(v)

compararLaterales(v)