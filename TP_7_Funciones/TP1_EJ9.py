import random

def generarNaranjas(total):
    naranjasCamion = []
    naranjasJugo = []
    pesoNaranjas = 0
    for i in range(total):
        n = random.randint(150, 350)
        if n < 200 or n > 300:
            naranjasJugo.append(n)
        else:
            pesoNaranjas += n
            naranjasCamion.append(n)
    return naranjasCamion, naranjasJugo, pesoNaranjas

cajones = lambda cant: cant // 100
sobrantes = lambda cant: cant % 100
camiones = lambda peso: peso // 500000
excedente = lambda peso: peso % 500000

# PROGRAMA PRINCIPAL
cantNaranjas = int(input("Ingrese la cantidad de naranjas: "))
naranjasCamion, naranjasJugo, pesoNaranjas = generarNaranjas(cantNaranjas)
cantJugo = len(naranjasJugo)
cantNaranjas = len(naranjasCamion)
 
cantCamiones = camiones(pesoNaranjas)
cantExcedente = excedente(pesoNaranjas)

if cantExcedente >= 400000:
    cantCamiones += 1

print("Total cajones:", cajones(cantNaranjas))
print("Total naranjas para jugo:", cantJugo)
print("Naranjas sobrantes:", sobrantes(cantNaranjas))
print("Camiones necesarios:", cantCamiones)