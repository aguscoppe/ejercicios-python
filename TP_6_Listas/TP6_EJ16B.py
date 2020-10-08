import random

def crearNumero():
    n = random.randint(1, 50)
    return n

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
    seguirJugando = False
    if res == "S":
        intentos = adivinarNumero()
        seguirJugando = True
    elif res == "N":
        print("Juego finalizado")
        intentos = 0
    return intentos, seguirJugando

def verPuntajesMaximos(lista):
    cant = 5
    if len(lista) < 5:
        cant = len(lista)
    for i in range(cant):
        print("Jugador:", lista[i][0], "| Intentos:", lista[i][1])

puntajeTotal = []
puntos, seguirJugando = iniciarJuego()
while seguirJugando:
    puntaje = []
    if puntos > 0:
        nombre = input("Ingrese su nombre: ")
        puntaje.append(nombre)
        puntaje.append(puntos)
        puntajeTotal.append(puntaje)
        verPuntajesMaximos(puntajeTotal)
    puntos, seguirJugando = iniciarJuego()