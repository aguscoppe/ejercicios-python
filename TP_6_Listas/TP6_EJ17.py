import random

def crearNumero():
    n = random.randint(1000, 9999)
    return n

def esAproximado(n, a):
    hayAproximados = False
    aproximados = 0
    copiaN = n
    while copiaN > 0:
        digitoN = copiaN % 10
        copiaN = copiaN // 10
        copiaA = a
        while copiaA> 0:
            digitoA = copiaA % 10
            copiaA = copiaA // 10
            if digitoN == digitoA:
                aproximados += 1
                hayAproximados = True
    return aproximados, hayAproximados

def esCorrecto(n, a):
    hayCorrectos = False
    correctos = 0
    copiaN = n
    copiaA = a
    while copiaN > 0:
        digitoN = copiaN % 10
        copiaN = copiaN // 10
        digitoA = copiaA % 10
        copiaA = copiaA // 10
        if digitoN == digitoA:
            correctos += 1
            hayCorrectos = True
    return correctos, hayCorrectos
        
def adivinarNumero():
    intentos = 1
    n = crearNumero()
    a = int(input("Ingrese un número entre 1000 y 9999 o -1 para finalizar: "))
    while a != -1:
        aproximados, hayAproximados = esAproximado(n, a)
        correctos, hayCorrectos = esCorrecto(n, a)
        if hayCorrectos and correctos == 4:
            break
        if hayAproximados:
            print("Hay", aproximados, "número(s) aproximado(s)")
        else:
            print("No hay números aproximados")
        if hayCorrectos:
            print("Hay", correctos, "número(s) correcto(s)")
        else:
            print("No hay números correctos")
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