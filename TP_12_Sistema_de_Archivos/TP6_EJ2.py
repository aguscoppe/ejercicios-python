import random

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%5d" %matriz[f][c], end="")
        print()

def fechaValida(d, m):
    esValida = True
    if (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
        esValida = False
    elif m == 2 and d > 29:
        esValida = False
    return esValida       

def generarDatos():
    generarNumero = lambda a, b: random.randint(a, b)
    datos = []
    contador = 0
    lluviaTotal = 0
    registros = generarNumero(50, 200)
    while contador != registros:
        dato = []
        dia = generarNumero(1, 31)
        mes = generarNumero(1, 12)
        while not fechaValida(dia, mes):
            dia = generarNumero(1, 31)
        lluvia = generarNumero(0, 1000)
        lluviaTotal += lluvia
        dato.append(dia)
        dato.append(mes)
        dato.append(lluvia)
        datos.append(dato)
        contador += 1
    return datos, lluviaTotal

def grabarArchivo(datos):
    try:
        arch = open("TP6_EJ2.csv", "wt")
        for dato in datos:
            arch.write(f"{dato[0]};{dato[1]};{dato[2]}\n")
        print("Archivo creado exitosamente")
    except OSError as mensaje:
        print(f"No se puede grabar el archivo: {mensaje}")
    finally:
        try:
            arch.close()
        except NameError:
            pass

def leerArchivo():
    try:
        arch = open("TP6_EJ2.txt", "rt")
        datos = []
        for linea in arch:
            dato = []
            dia, mes, lluvia = linea.split(";")
            lluvia = lluvia.rstrip("\n")
            dato.append(dia)
            dato.append(mes)
            dato.append(lluvia)
            datos.append(dato)
        print("Archivo leído exitosamente")
    except FileNotFoundError as mensaje:
        print(f"No se puede abrir el archivo: {mensaje}")
    except OSError as mensaje:
        print(f"No se puede leer el archivo: {mensaje}")
    finally:
        try:
            arch.close()
        except NameError:
            pass
    return datos

def ordenarDatos(datos, matriz):
    for dato in datos:
        d = int(dato[0])
        m = int(dato[1])
        lluvia = dato[2]
        matriz[d-1][m-1] = int(lluvia)

# PROGRAMA PRINCIPAL
listaDatos, lluviaTotal = generarDatos()
grabarArchivo(listaDatos)
matriz = [[0] * 12 for i in range(31)]
listaDatos = leerArchivo()
ordenarDatos(listaDatos, matriz)
print()
imprimirMatriz(matriz)
print()
print(f"Lluvia caída en todo el año: {lluviaTotal}")