def intercalarListas(lista1, lista2):
    x = 0
    for i in range(len(lista1) + len(lista2)):
        if i % 2 != 0:        
            lista1.insert(i, lista2[x:x+1])
            x += 1

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]

intercalarListas(lista1, lista2)

print(lista1)