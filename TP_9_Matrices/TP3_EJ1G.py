def calcularPromedioImpar(m, c):
    impares = 0
    porcentaje = 0
    for i in range(len(m[0])):
        if m[i][c] % 2 != 0:
            impares += 1
    if impares != 0:
        porcentaje = impares*100 / len(m[0])
    return porcentaje   

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
print("Porcentaje de elementos con valor impar:", calcularPromedioImpar(matriz, 0), "%")