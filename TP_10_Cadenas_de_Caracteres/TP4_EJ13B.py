def calcularBillon(n):
    c = ""
    n = 0
    return c, n

def calcularMillon(n):
    c = ""
    n = 0
    return c, n

def calcularMillar(n):
    c = ""
    n = 0
    return c, n

def calcularCentena(n):
    c = ""
    res = n // 100
    if res > 1:
        c, a = calcularUnidad(res)
        c += "cientos"
        n -= 100*res
    else:
        c += "cien "
        n -= 100
    return c, n

def calcularDecena(n):
    c = ""
    n = 0
    return c, n

def calcularUnidad(n):
    c = ""
    if n == 9:
        c += "nueve"
    elif n == 8:
        c += "ocho"
    elif n == 7:
        c += "siete"
    elif n == 6:
        c += "seis"
    elif n == 5:
        c += "cinco"
    elif n == 4:
        c += "cuatro"
    elif n == 3:
        c += "tres"
    elif n == 2:
        c += "dos"
    else:
        c += "uno"
    return c, n

def convertirNumero(n):
    c = ""
    while n > 0:
        if n == 1000000000000:
            c, n = calcularBillon(n)
        elif n >= 1000000:
            c, n = calcularMillon(n)
        elif n >= 1000:
            c, n = calcularMillar(n)
        elif n >= 100:
            c, n = calcularCentena(n)
        elif n >= 10:
            c, n = calcularDecena(n)
        else:
            c, n = calcularUnidad(n)
    return c

# PROGRAMA PRINCIPAL
n = 509
print(convertirNumero(n))