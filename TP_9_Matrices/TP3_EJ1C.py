def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

def intercambiarFilas(m, f1, f2):
    aux = m[f1]
    m[f1] = m[f2]
    m[f2] = aux

def crearMatriz():
    matriz = []
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))
    for i in range(filas):
        fila = []
        for j in range(columnas):
            n = int(input("Ingrese un número: "))
            fila.append(n)
        matriz.append(fila)
    return matriz

# PROGRAMA PRINCIPAL
matriz = crearMatriz()
intercambiarFilas(matriz, 0, 1)
print()
imprimirMatriz(matriz)