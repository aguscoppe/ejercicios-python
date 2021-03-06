def ingresarFecha():
    d = int(input("Ingrese el día: "))
    m = int(input("Ingrese el mes: "))  
    a = int(input("Ingrese el año: "))
    return d, m, a

def diaSiguiente(d, m, a):
    if d == 31 and m == 12:
        d = 1
        m = 1
        a += 1
    elif d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10):
        d = 1
        m += 1
    elif d == 30 and (m == 4 or m == 6 or m == 9 or m == 11):
        d = 1
        m += 1
    elif (d == 28 or d == 29) and m == 2:
        d = 1
        m += 1
    else:
        d += 1
    return d, m, a

def calcularDias(dA, mA, aA, dB, mB, aB):
    cant = 0
    if aA > aB:
        dC, mC, aC = dA, mA, aA
        dA, mA, aA = dB, mB, aB
        dB, mB, aB = dC, mC, aC

    while(dA != dB or mA != mB or aA != aB):
        dA, mA, aA = diaSiguiente(dA, mA, aA)
        cant += 1
    return cant

# Programa principal
print("Primera fecha")
d1, m1, a1 = ingresarFecha()
print("Segunda fecha")
d2, m2, a2 = ingresarFecha()
cantDias = calcularDias(d1, m1, a1, d2, m2, a2)
print("Cantidad de días entre ambas fechas:", cantDias)