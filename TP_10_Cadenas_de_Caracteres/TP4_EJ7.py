def conRebanadas(c, i, n):
    n = n + i
    return c[i:n]

def sinRebanadas(c, i, n):
    n = n + i
    nueva = ""
    for i in range(i, n):
        nueva += c[i]
    return nueva

# PROGRAMA PRINCIPAL
c = "Oid mortales el grito sagrado"
i = int(input("Índice: "))
n = int(input("Cantidad de caracteres: "))

print(conRebanadas(c, i, n))
print(sinRebanadas(c, i, n))