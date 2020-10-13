def crearListaPalabras():
    lista = []
    cant = int(input("Ingrese cuántas palabras tendrá la lista: "))
    for i in range(cant):
        p = input("Ingrese una palabra: ")
        lista.append(p)
    return lista

def eliminarPalabras(l1, l2):
    for i in range(len(l2)):
        while l2[i] in l1:
            l1.remove(l2[i])

# PROGAMA PRINCIPAL
listaA = crearListaPalabras()
listaB = crearListaPalabras()
print()
print("Lista original:", listaA)
print("Palabras a borrar:", listaB)
eliminarPalabras(listaA, listaB)
print("Lista resultante:", listaA)