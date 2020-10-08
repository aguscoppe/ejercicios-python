import random

def generarSecuencia(cant):
    lista = []
    while cant > 0:
        n = random.randint(1, 20)
        lista.append(n)
        cant -= 1
    return lista

def insertarCeros(lista):
    LIMITE = 20
    nuevaLista = []
    cont = 0
    for i in range(len(lista)):
        cont = cont + lista[i]
        if cont <= LIMITE:
            nuevaLista.append(lista[i])
        else:
            nuevaLista.append(0)
            nuevaLista.append(lista[i])
            cont = lista[i]
    nuevaLista.append(0)
    return nuevaLista

# devuelve la cantidad máxima de elementos en la secuencia recibida
# sin contar los ceros
def mayorSecuencia(secuencia):
    cont = 0
    secuenciaMaxima = 0
    for i in range (len(secuencia)):
        if secuencia[i] != 0:
            cont += 1
        else:
            if cont > secuenciaMaxima:
                secuenciaMaxima = cont
            cont = 0
    return secuenciaMaxima

# crea mini secuencias a partir de la cantidad indicada por la función mayorSecuencia
def cortarSecuencia(cant, lista):
    cont = 0
    nuevaLista = []
    for i in range (len(lista) - 1):
        if cont == cant and lista[i] == 0:
            print(nuevaLista)
            nuevaLista = []
            cont = 0
        elif lista[i] == 0:
            nuevaLista = []
            cont = 0
        elif lista[i] != 0:
            nuevaLista.append(lista[i])
            cont += 1
        
n = int(input("Ingresar cantidad de elementos que tendrá la lista: "))

secuencia = generarSecuencia(n)

secuencia = insertarCeros(secuencia)

print(secuencia)

maxima = mayorSecuencia(secuencia)

cortarSecuencia(maxima, secuencia)