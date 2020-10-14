def calcularPromedio(m, f):
    return sum(m[f]) / len(m[f])

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
print()
print("Promedio de la fila 0:", calcularPromedio(matriz, 0))