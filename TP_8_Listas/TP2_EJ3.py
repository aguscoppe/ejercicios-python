def crearCuadrados(limite):
    n = 1
    lista = []
    while n <= limite:
        lista.append(n**2)
        n += 1
    return lista
    
def imprimirUltimos(lista, n):
    if len(lista) < n:
        print(lista)
    else:
        longitud = len(lista)
        for i in range((longitud-n), longitud):
            print(lista[i])

# PROGRAMA PRINCIPAL
n = int(input("Ingrese un número entero positivo: "))
lista = crearCuadrados(n)
imprimirUltimos(lista, 10)