def normalizar(lista):
    total = sum(lista)
    normalizada = []
    if total != 0:
        for i in range(len(lista)):
            normalizada.append(lista[i] / total)
    return normalizada

listaA = [1, 1, 2]
listaB = [5, 10, 15, 20]

print(normalizar(listaA))
print(normalizar(listaB))