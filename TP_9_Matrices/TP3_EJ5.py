# FILAS - Numeros
# COLUMNAS = Letras

import random

def butacasLibres(matriz):
    filas = len(matriz)
    total = 0
    actualLibres = 0
    mayorLibres = -1
    indiceContiguas = 0
    for f in range(filas):
        actualLibres = matriz[f].count(0)
        total += actualLibres
        if mayorLibres < actualLibres:
            mayorLibres = actualLibres
            indiceContiguas = f + 1
    return total, indiceContiguas

def reservar(matriz, butaca):
    print()
    columnas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = butaca[0]
    c = columnas.index(c)
    f = int(butaca[1]) - 1
    if matriz[f][c] == 0:
        matriz[f][c] = 1
        return True
    return False

def cargarSala(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, 1)
           
def mostrarButacas(matriz):
    print()
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
    print()

def administrarFunciones():
    pass

# PROGRAMA PRINCIPAL
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de butacas: "))

matriz = [[0] * columnas for i in range(filas)]

cargarSala(matriz)

mostrarButacas(matriz)

butaca = input("Ingrese la butaca que quiere reservar con una letra y un número (Ej. B3): ")
while not reservar(matriz, butaca):
    print("Esa butaca no está disponible.")
    butaca = input("Ingrese otra butaca para reservar (Ej. B3): ")
print()
print(f"La butaca {butaca} fue reservada con éxito.")

mostrarButacas(matriz)

libres, contiguas = butacasLibres(matriz)
print(f"Cantidad de butacas libres: {libres}")
print()
print(f"Secuencia más larga de butacas libres contiguas: Fila {contiguas}")