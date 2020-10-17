def esCapicua(cadena):
    i = 0
    j = len(cadena) - 1
    esCapicua = True
    while i < j:
        if cadena[i] != cadena[j]:
            esCapicua = False
            break
        i += 1
        j -= 1
    return esCapicua

c = input("Ingrese una palabra: ")

if esCapicua(c):
    print(c, "es capicúa")
else:
    print(c, "no es capicúa")