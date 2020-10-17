def ordenarAlfabeticamente(c):
    lista = c.split()
    lista.sort()
    nueva = " ".join(lista)
    return nueva

# PROGRAMA PRINCIPAL
cadena = "oid   mortales      el grito         sagrado"
print(ordenarAlfabeticamente(cadena))