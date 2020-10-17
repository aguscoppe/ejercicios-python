def leerDirecciones():
    listaMail = []
    mail = input("Ingrese una dirección de mail: ")
    while mail != "":
        listaMail.append(mail)
        mail = input("Ingrese una dirección de mail: ")
    return listaMail

def verificarDireccion(mail):
    listaValidos = []
    mailValido = True
    if not mail.islower():
        mail = mail.lower()
    arrobas = 0
    for i in range (len(mail) - 1):
        if mail[i] == "@":
            arrobas += 1
    if arrobas != 1:
        mailValido = False
    else:
        usuario, dominio = mail.split("@")
        for i in range (len(dominio) - 1):
            if dominio[i + 1] == ".":
                indiceA = i
                break
        final = dominio[-7:]
        dominio = dominio[0:indiceA+1]
        if final != ".com.ar" or len(dominio) < 1 or not usuario.isalpha():
            mailValido = False
        if mailValido and dominio not in listaValidos:
            listaValidos.append(dominio)
    listaValidos.sort()
    return listaValidos

# PROGRAMA PRINCIPAL
listaMail = leerDirecciones()
print("Lista de dominios válidos:")
print(list(map(verificarDireccion, listaMail)))