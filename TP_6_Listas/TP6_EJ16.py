import random

def crearNumero():
    n = random.randint(1, 50)
    return n

def listaPuntajes(puntaje):
    lista.append(puntaje)
    return lista

def adivinarNumero():
    intentos = 1
    n = crearNumero()
    a = int(input("Ingrese un número entre 1000 y 9999 o -1 para finalizar: "))
    while a != -1:
        if n < a:
            print("El número es más pequeño")
        elif n > a:
            print("El número es más grande")
        else:
            break
        intentos += 1
        a = int(input("Ingrese un número entre 1000 y 9999 o -1 para finalizar: "))
    if a == -1:
        print("Juego abandonado")
        intentos = 0
        iniciarJuego()
    else:
        print("El número secreto era:", n)
        print("Cantidad total de intentos:", intentos)
    return intentos
        
def iniciarJuego():
    res = input("¿Desea jugar una partida? (S/N): ")
    if res == "S":
        intentos = adivinarNumero()
    elif res == "N":
        print("Juego finalizado")
        intentos = 0
    return intentos

def ordenamientoBurbujeo(lista):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range (len(lista) - 1):
            if lista[i] < lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                desordenado = True
    return lista

def leerMejoresPuntajes(puntajes):
    puntajes = ordenamientoBurbujeo(puntajes)
    for i in range(5):
        print(i + 1, "° puesto:", puntajes[i], "intentos")

listaPuntajes = [0, 0, 0, 0 ,0]
puntaje = iniciarJuego()
puntajeMaximo = 0
if puntaje > 0:
    listaPuntajes.append(puntaje)
    leerMejoresPuntajes(listaPuntajes)