import math

def devolverRaiz(n):
    return math.sqrt(n)

# PROGRAMA PRINCIPAL
while True:
    try:
        n = int(input("Ingrese un número: "))
        # if not n >= 0...
        assert n >= 0
        break
    except AssertionError:
        print("El número debe ser positivo.")

print()
print(f"Raíz cuadrada de {n}: {devolverRaiz(n)}")