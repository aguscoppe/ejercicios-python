def descifrarClave(clave):
    clave1 = ""
    clave2 = ""
    for i in range(len(clave)):
        if i % 2 != 0:
            clave1 += clave[i]
        else:
            clave2 += clave[i]
    return clave1, clave2

# PROGRAMA PRINCIPAL
claveMaestra = input("Ingrese la clave maestra: ")
c1, c2 = descifrarClave(claveMaestra)
print("Primera clave:", c1)
print("Segunda clave:", c2)