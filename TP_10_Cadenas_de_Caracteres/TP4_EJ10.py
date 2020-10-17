def reemplazarApariciones(c, p, r):
    cant = 0
    listaPalabras = c.split()
    for i in range(len(listaPalabras)):
        if listaPalabras[i] == p:
            listaPalabras[i] = r
            cant += 1
    resultado = " ".join(listaPalabras)
    return resultado, cant

# PROGRAMA PRINCIPAL
cadena = input("Ingrese texto: ")
palabra = input("Elija una palabra de la cadena: ")
reemplazo = input("Ingrese la palabra para realizar el reemplazo: ")

resultado, cantidad = reemplazarApariciones(cadena, palabra, reemplazo)
print()

if cantidad == 0:
    print("Esa palabra no está en el texto ingresado")
else:
    print("Cantidad de apariciones:", cantidad)
    print("Nueva cadena:", resultado)