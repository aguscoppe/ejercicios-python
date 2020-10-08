def crearLista():
    n = int(input("Ingrese un número entre 1 y 20: "))
    MENOR = 1
    MAYOR = 20
    lista = []    
    while n != -1:
        if n < MENOR or n > MAYOR:
            print("El número está fuera de rango")
        else:
            lista.append(n)
        n = int(input("Ingrese un número entre 1 y 20: "))        
    return lista

def invertirNumero(n):
    digito = 0
    resultado = 0
    while n != 0:
        digito = n % 10
        n = n // 10
        resultado = digito + resultado * 10
    return resultado

def invertirPosImpar():
    lista = crearLista()    
    if len(lista) <= 1:
        return 0
    for i in range (len(lista)):
        if i % 2 != 0:
            lista[i] = invertirNumero(lista[i])    
    return lista

nuevaLista = invertirPosImpar()

if nuevaLista == 0:
    print("La lista no tiene posiciones impares")
else:
    print(nuevaLista)