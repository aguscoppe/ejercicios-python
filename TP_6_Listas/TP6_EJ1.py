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

print(crearLista())