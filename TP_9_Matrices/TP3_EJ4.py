import random

def crearMatriz():
    n = int(input("Ingrese la cantidad de fábricas: "))
    filas = n
    columnas = 6
    matriz = [[0] * columnas for i in range(filas)]
    return matriz

def rellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, 150)

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="  ")
        print()

def mayorFabricacion(matriz):
    fila = 0
    for f in range(len(matriz)):
        fila = sum(matriz[f])
        print("Fábrica", f + 1, "- Total de bicicletas:", fila)

def diaProductivo(matriz):
    mayor = -1
    fabrica = -1
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] > mayor:
                mayor = matriz[f][c]
                fabrica = f
                dia = c
    print("El día de mayor producción fue el día", dia, "de la fábrica", fabrica + 1)

def columnaProductiva(matriz):
    totales = [0, 0, 0, 0, 0, 0]
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            totales[c] += matriz[f][c]
    maximo = max(totales)
    dia = totales.index(maximo)
    print("El día semanal más productivo para todas las fábricas fue el n°", dia)

def menosFabricadas(matriz):
    menos = []
    for f in range(len(matriz)):
        menos.append(min(matriz[f]))
    return menos

# PROGRAMA PRINCIPAL
matriz = crearMatriz()
rellenarMatriz(matriz)
print()
imprimirMatriz(matriz)
print()
mayorFabricacion(matriz)
print()
diaProductivo(matriz)
print()
columnaProductiva(matriz)
print()
menos = menosFabricadas(matriz)
for i in range(len(menos)):
    print("Fábrica", i + 1, "- Menor cantidad producida:", menos[i])