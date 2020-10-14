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
    maximo = len(matriz[0]) -1
    for f in range(filas):
        for c in range(columnas):
            if c >= maximo:
                matriz[f][c] = n
                n += 1
                if c == (len(matriz[0]) - 1):
                    maximo -= 1
        
def crearMatriz():
    n = int(input("Ingrese el tamño de la matriz: "))
    filas = n
    columnas = n
    matriz = [[0] * columnas for i in range(filas)]
    return matriz

# PROGRAMA PRINCIPAL
matriz = crearMatriz()
rellenarMatriz(matriz)
print()
imprimirMatriz(matriz)