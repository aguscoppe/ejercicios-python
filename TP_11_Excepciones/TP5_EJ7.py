import random

def adivinarNumero(numCorrecto):
    n = 0
    intentos = 0
    while n != numCorrecto:
        intentos += 1
        try:
            n = int(input("Ingrese un número entre 1 y 500: "))
            if n < numCorrecto:
                print("El número secreto es mayor.")
            elif n > numCorrecto:
                print("El número secreto es menor.")
            else:
                break
        except ValueError:
            print("Solo deben ingresarse números enteros.")
    return intentos

# PROGRAMA PRINCIPAL
generarNumero = lambda a, b: random.randint(a, b)
n = generarNumero(1, 500)
intentos = adivinarNumero(n)

print()
print(f"¡Ganaste! El número secreto era {n}.")

print()
print(f"Intentos totales: {intentos}")