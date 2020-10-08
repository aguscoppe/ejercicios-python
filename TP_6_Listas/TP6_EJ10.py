import random

# crea dos listas llenas con números aleatorios
def llenarListas(n):
    a = []
    b = []
    for i in range (n):
        a.append(random.randint(1, 20))
        b.append(random.randint(1, 20))
    return a, b

# invierte valor dado
def invertirValor(n):
    nuevo = 0
    while n != 0:
        digito = n % 10
        n = n // 10
        nuevo = nuevo * 10 + digito
    return nuevo

# concatena (c) pares de a  con impares de b
# concatena (d) pares de a y pares invertidos de b
def concatenarValores(a, b):
    c = []
    d = []
    for i in range (len(a)):
        if a[i] % 2 == 0:
            c.append(a[i])
            d.append(a[i])
    for i in range (len(b)):
        if b[i] % 2 != 0:
            c.append(b[i])
        else:
            invertido = invertirValor(b[i])
            d.append(invertido)
    return c, d

# intercala valores de a y b en una nueva lista
def intercalarValores(a, b):
    nuevaLista = []
    for i in range (len(a)):
        nuevaLista.append(a[i])
        nuevaLista.append(b[i])
    return nuevaLista

n = int(input("Ingrese la cantidad de elementos que tendrán las listas: "))

a, b = llenarListas(n)

c, d = concatenarValores(a, b)

e = intercalarValores(a, b)

print("Valores pares de A con impares de B:", c)
print("Valores pares de A con el reverso de los valores pares de B:", d)
print("Valores de A y B intercalados:", e)