# EJERCICIO 3

def crearLista():
    n = int(input("Ingrese un número entre 1 y 20 o -1 para finalizar: "))
    MENOR = 1
    MAYOR = 20
    lista = []    
    while n != -1:
        if n < MENOR or n > MAYOR:
            print("El número está fuera de rango")
        else:
            lista.append(n)
        n = int(input("Ingrese un número entre 1 y 20 o -1 para finalizar: "))        
    return lista

def esCapicua():
    lista = crearLista()
    resultado = 1
    if len(lista) == 0:
        resultado = 0
        return resultado
    j = len(lista) - 1    
    for i in range (j):
        if lista[i] != lista[j]:
            resultado = -1
            break
        j = j - 1    
    return resultado

resultadoCapicua = esCapicua()

print()
if resultadoCapicua == 1:
    print("La lista es capicúa")
elif resultadoCapicua == -1:
    print("La lista no es capicúa")
else:
    print("La lista está vacía")