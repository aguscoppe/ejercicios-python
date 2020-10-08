# EJERCICIO 3

def imprimirAsteriscos(altura):
    while altura > 0:
        print("*")
        altura = altura - 1

n = int(input("Ingrese la altura: "))
imprimirAsteriscos(n)