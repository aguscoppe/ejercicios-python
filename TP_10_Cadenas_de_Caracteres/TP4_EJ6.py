def conRebanadas(c, i, n):
    n = n + i
    sub = c[i:n]
    return sub

def sinRebanadas(c, i, n):
    n = n + i
    nueva = ""
    for i in range(i, n):
        nueva += c[i]
    return nueva

# PROGRAMA PRINCIPAL
cadena = "Oid mortales el grito sagrado"
pos = int(input("Ingrese la posición de inicio de la subcadena: "))
cant = int(input("Ingrese la cantidad de caracteres para extraer: "))

print(conRebanadas(cadena, pos, cant))
print(sinRebanadas(cadena, pos, cant))