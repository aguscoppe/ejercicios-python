def esDiagonalSimetrica(m):
    if len(m) == len(m[0]):
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
print()
if esDiagonalSimetrica(matriz):
    print("La matriz es simétrica con respecto a su diagonal principal")
else:
    print("La matriz no es simétrica con respecto a su diagonal principal")