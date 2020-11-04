def crearLista():
    n = int(input("Ingrese un número entero o -1 para finalizar: "))
    lista = []
    while n != -1:
        lista.append(n)
        n = int(input("Ingrese un número entero o -1 para finalizar: "))
    return lista

def buscarNumero(lista):
    limite = 3
    errores = 0
    while errores < limite:
        n = int(input("Ingrese un número para ver su posición en la lista: "))
        try:
            pos = lista.index(n)
            print(f"Posición del número {n} en la lista: {pos}")
        except ValueError:
            print("El número ingresado no está en la lista.")
            errores += 1

# PROGRAMA PRINCIPAL
lista = crearLista()
print()
print(*lista)

print()
buscarNumero(lista)