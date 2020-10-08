# EJERCICIO 34

d = int(input("Ingrese un día: "))
m = int(input("Ingrese un mes: "))
a = int(input("Ingrese un año: "))
n = int(input("Ingrese una cantidad de días: "))
fechaValida = False
cantDias = 31

# programa para verificar validez de la fecha
if m == 4 or m == 6 or m == 9 or m == 11:
    cantDias = 30
elif m == 2:
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        cantDias = 29
    else:
        cantDias = 28

if d < 1 or d > cantDias or m < 1 or m > 12:
    fechaValida = False
else:
    fechaValida = True

# programa para calcular la nueva fecha
if fechaValida == True:
    d = d + n
    while d > 31:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if m == 12:
                m = 1
                a += 1
            else:
                m += 1
            d -= 31
        elif m == 4 or m == 6 or m == 9 or m == 11:
            m += 1
            d -= 30
        else:
            m += 1
            if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
                d -= 29
            else:
                d -= 28

    if d > 30 and (m == 4 or m == 6 or m == 9 or m == 11):
        d = 1
        m += 1
    elif m == 2 and d > 28:
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            d = 29
        else:
            d = 1
            m += 1

    print("La fecha resultante es:", d, "/", m, "/", a)
else:
    print("La fecha ingresada es inválida")