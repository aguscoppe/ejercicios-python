def registrarSocios():
    listaSocios = []
    numSocio = int(input("Ingrese el número de socio: "))
    while numSocio != -1:
        listaSocios.append(numSocio)
        numSocio = int(input("Ingrese el número de socio: "))
    return listaSocios

def contarIngresos(lista):
    vistos = []
    for i in range(len(lista)):
        if lista[i] not in vistos:
            print("El socio", lista[i], "ingresó", lista.count(lista[i]), "veces")
        vistos.append(lista[i])

def eliminarSocio(n, lista):
    while n in lista:
        lista.remove(n)

# PROGRAMA PRINCIPAL
listaSocios = registrarSocios()
print()
contarIngresos(listaSocios)
print()
socioEliminar = int(input("Ingrese el socio que quiere eliminar: "))
eliminarSocio(socioEliminar, listaSocios)
print()
print("Se eliminó el socio", socioEliminar)
print()
contarIngresos(listaSocios)