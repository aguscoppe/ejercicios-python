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

def calcularSuma():
    lista = crearLista()
    total = 0    
    for i in range (len(lista)):
        total = total + lista[i]    
    return total

print("El resultado de la suma de los números de la lista es:", calcularSuma())