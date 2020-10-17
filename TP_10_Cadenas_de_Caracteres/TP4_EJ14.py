def leerDirecciones():
    listaMail = []
    mail = input("Ingrese una dirección de mail: ")
    while mail != "":
        listaMail.append(mail)
        mail = input("Ingrese una dirección de mail: ")
    return listaMail

def verificarDirecciones(listaMail):
    listaValidos = []
    for mail in listaMail:
        mailValido = True
        if not mail.islower():
            mail = mail.lower()
        indiceA = 0
        indiceB = 0
        arrobas = 0
        for i in range (len(mail) - 1):
            if mail[i + 1] == "@":
                indiceA = i
                indiceB = i + 2
            if mail[i] == "@":
                arrobas += 1
        usuario = mail[0:indiceA+1]
        dominio = mail[indiceB:]
        if arrobas != 1 or not usuario.isalpha():
            mailValido = False
        else:
            for i in range (len(dominio) - 1):
                if dominio[i + 1] == ".":
                    indiceA = i
                    break
            final = dominio[-7:]
            dominio = dominio[0:indiceA+1]
            if final != ".com.ar" or len(dominio) < 1:
                mailValido = False
            if mailValido and dominio not in listaValidos:
                listaValidos.append(dominio)
    listaValidos.sort()
    return listaValidos

# PROGRAMA PRINCIPAL
listaMail = leerDirecciones()
lista = verificarDirecciones(listaMail)
print("Lista de dominios válidos:")
print(*lista)