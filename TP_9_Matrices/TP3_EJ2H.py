def rellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    n = 1
    limite = 1
    for f in range(0, limite):
        for c in range(limite, -columnas - 1, -1):
            matriz[f][c] = n
            n += 1
        limite += 1

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

# PROGRAMA PRINCIPAL
filas = int(input("Ingrese la cantidad de filas y columnas: "))
matriz = [[0] * filas for i in range(filas)]

rellenarMatriz(matriz)
imprimirMatriz(matriz)