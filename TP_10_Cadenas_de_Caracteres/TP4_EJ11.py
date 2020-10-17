def buscarSubcadena(cad, sub):
    cad = cad.lower()
    sub = sub.lower()
    cant = 0
    indice = 0
    for letra in cad:
        if letra == sub[indice]:
            if indice < len(sub) - 1:
                indice += 1
            else:
                indice = 0
                cant += 1
    return cant

# PROGRAMA PRINCIPAL

#cadena = input("Ingrese la cadena: ")
#subcadena = input("Ingrese la sub cadena: ")

cadena = "pato pato ñato"
subcadena = "ao"

cantidad = buscarSubcadena(cadena, subcadena)
print(f"Cantidad encontrada: {cantidad}")