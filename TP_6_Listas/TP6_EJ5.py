def leerFecha():
    d = int(input("Ingrese el día del cumpleaños: "))
    m = int(input("Ingrese el mes del cumpleaños: "))
    a = int(input("Ingrese el año del cumpleaños: "))
    return d, m, a

def verificarFecha(d, m, a):
    if d < 0 or d > 31:
        return False
    elif m < 0 or m > 12:
        return False
    elif a < 0:
        return False
    return True

def contarCumples():    
    legajo = int(input("Ingrese el número de legajo del alumno o -1 para finalizar: "))
    listaCumples = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
    while legajo != -1:
        d, m, a = leerFecha()        
        if verificarFecha(d, m, a) == True:
            listaCumples[m-1] = listaCumples[m-1] + 1
        legajo = int(input("Ingrese el número de legajo del alumno o -1 para finalizar: "))    
    return listaCumples

def emitirInforme(lista):
    for i in range (len(lista)):
        print("En el mes", i+1, "hay", lista[i], "cumpleaños")    

listaCumples = contarCumples()
emitirInforme(listaCumples)