def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

def esPalindromo(matriz):
    for i in range(len(matriz)):
        columna = []
        for j in range(len(matriz[i])):
            columna.append(matriz[j][i])
        copiaInversa = columna[::-1]
        if copiaInversa == columna:
            return True
        return False

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
print(esPalindromo(matriz))
imprimirMatriz(matriz)