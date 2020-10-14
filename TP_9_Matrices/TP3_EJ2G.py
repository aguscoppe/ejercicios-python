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
    n = 1
    for f in range(filas):
        for c in range(columnas):
            if f == 0:
                matriz[f][c] = n
                n += 1
            if c == (len(matriz[0]) - 1) and matriz[f][c] == 0:
                matriz[f][c] = n
                n += 1
    for f in range(filas):
        for c in range(-1, -columnas-1, -1):
            if f == (len(matriz[0]) - 1) and matriz[f][c] == 0:
                matriz[f][c] = n
                n += 1
    for f in range(-1, -filas-1, -1):
        for c in range(columnas):
            if c == 0:
                if matriz[f][c] == 0:
                    matriz[f][c] = n
                    n += 1
    for f in range(filas):
        for c in range(columnas):
            if f == 1 and matriz[f][c] == 0:
                matriz[f][c] = n
                n += 1
        
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