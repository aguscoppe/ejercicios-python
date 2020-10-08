def ordenarInsercion(lista):
    for i in range (1, len(lista)):
        aux = lista[i]
        j = i
        while j > 0 and lista[j-1] > aux:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = aux
    return lista

def crearLista():
    n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    lista = []
    while n != -1:
        lista.append(n)
        n = int(input("Ingrese un número para agregar a la lista o -1 para finalizar: "))
    return lista

def intercalarListas(m, n):
    nuevaLista = []
    i = 0
    j = 0
    while len(nuevaLista) != (len(m) + len(n)):
        if len(nuevaLista) == len(m) + len(n) - 2:
            if m[i] <= n[j]:
                nuevaLista.append(m[i])
                nuevaLista.append(n[j])
            else:
                nuevaLista.append(n[j])
                nuevaLista.append(m[i])               
        elif m[i] <= n[j]:
            nuevaLista.append(m[i])
            if i < (len(m) - 1):
                i = i + 1
        elif n[j] <= m[i]:
            nuevaLista.append(n[j])
            if j < (len(n) - 1):
                j = j + 1
    return nuevaLista

m = crearLista()
n = crearLista()

m = ordenarInsercion(m)
n = ordenarInsercion(n)

print()

print("Primera lista:", m)
print("Segunda lista:", n)
print("Lista intercalada:", intercalarListas(m, n))