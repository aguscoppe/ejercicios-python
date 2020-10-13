def verificarAscendente(lista):
    if lista == sorted(lista):
        return True
    return False

listaAsc = [1, 2, 3]
listaDesc = ["c", "b", "a"]
listaDesordenada = [5, 8, 9, 1, 2, 4, 10]

print(verificarAscendente(listaAsc))
print(verificarAscendente(listaDesc))
print(verificarAscendente(listaDesordenada))