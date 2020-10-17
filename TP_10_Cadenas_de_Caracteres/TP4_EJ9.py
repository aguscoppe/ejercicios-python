def devolverSubcadena(c, n):
    indice = len(c) - n
    return c[indice:]

# PROGRAMA PRINCIPAL
c = input("Ingrese texto: ")
n = int(input("Ingrese un número entero: "))

print("Últimos", n, "caracteres:", devolverSubcadena(c, n))