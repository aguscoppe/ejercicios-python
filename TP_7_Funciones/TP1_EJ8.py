def diaDeLaSemana(dia,mes,año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

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

def imprimirCalendario(m, a):
    d = 1
    dia = ""
    copiaMes = m
    copiaAño = a
    while(m == copiaMes and a == copiaAño):
        diaSem = diaDeLaSemana(d,m,a)
        if diaSem == 0:
            dia = "Domingo"
        elif diaSem == 1:
            dia = "Lunes"
        elif diaSem == 2:
            dia = "Martes"
        elif diaSem == 3:
            dia = "Miércoles"
        elif diaSem == 4:
            dia = "Jueves"
        elif diaSem == 5:
            dia = "Viernes"
        else:
            dia = "Sábado"
        print(dia, ", ", d, "/", m, "/", a, sep="")
        d, m, a = diaSiguiente(d, m, a)

m = int(input("Ingrese el mes: "))  
a = int(input("Ingrese el año: "))
imprimirCalendario(m, a)