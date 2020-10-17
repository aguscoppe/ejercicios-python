def transformarNumero(n):
    cadena = ""
    numeros = [1000000000000, 1000000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100,
               90, 80, 70, 60, 50, 40, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17,
               16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    palabras = ["billon", "millon", "mil", "novecientos", "ochocientos", "setecientos", "seiscientos",
                "quinientos", "cuatrocientos", "trescientos", "doscientos", "cien", "noventa",
                "ochenta", "setenta", "sesenta", "cincuenta", "cuarenta", "treinta", "veintinueve",
                "veintiocho", "veintisiete", "veintiséis", "veinticinco", "veinticuatro",
                "veintitrés", "veintidos", "veintiuno", "veinte", "diecinueve", "dieciocho",
                "diecisiete", "dieciséis", "quince", "catorce", "trece", "doce", "once", "diez",
                "nueve", "ocho", "siete", "seis", "cinco", "cuatro", "tres", "dos", "uno", "cero"]
    i = 0
    while n > 0:
        if n >= numeros[i]:
            # BILLON O MILLON
            # MIL
            if n >= 2000:
                u = n // 1000
                indice = numeros.index(u)
                cadena += palabras[numeros.index(u)] + " "
                n -= n * u
            cadena += palabras[i] + " "
            n -= numeros[i]
        i += 1
    return cadena

# PROGRAMA PRINCIPAL
n = int(input("Ingrese un número del 1 al 1000000000000: "))
while n > 1000000000000 or n < 0:
    print("Error: Valor inválido")
    n = int(input("Ingrese un número del 1 al 1000000000000: "))
s = transformarNumero(n)
print(s)



#  
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800,
#           900, 1000, 1000000, 1000000000000]
#palabras = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
#            "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho",
#            "diecinueve", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta",
#            "ochenta", "noventa", "cien"]