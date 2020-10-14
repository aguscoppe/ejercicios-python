import random

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

def rellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    usados = []
    num = random.randint(0, filas**2)
    for f in range(filas):
        for c in range(columnas):
            while num in usados:
                num = random.randint(0, filas**2)
            if num not in usados:
                matriz[f][c] = num
            usados.append(num)
            num = random.randint(0, filas**2)

def crearMatriz():
    n = int(input("Ingrese el tamaño de la matriz: "))
    filas = n
    columnas = n
    matriz = [[0] * columnas for i in range(filas)]
    return matriz

# PROGRAMA PRINCIPAL
matriz = crearMatriz()
rellenarMatriz(matriz)
print()
imprimirMatriz(matriz)