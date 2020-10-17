# El número más grande que se puede escribir con estos símbolos es el 3999 = MMMCMXCIX.
# Para números con valores igual o superiores a 4000 se utiliza una rayita encima de las letras
# e indica tantos millares como unidades tenga este símbolo

def convertirRomano(num):
    resultado = ""
    while num > 0:
        if num >= 1000:
            resultado += "M"
            num -= 1000
        elif num >= 900:
            resultado += "CM"
            num -= 900
        elif num >= 500:
            resultado += "D"
            num -= 500
        elif num >= 400:
            resultado += "CD"
            num -= 400
        elif num >= 100:
            resultado += "C"
            num -= 100
        elif num >= 90:
            resultado += "XC"
            num -= 90
        elif num >= 50:
            resultado += "L"
            num -= 50
        elif num >= 40:
            resultado += "XL"
            num -= 40
        elif num >= 10:
            resultado += "X"
            num -= 10
        elif num >= 9:
            resultado += "IX"
            num -= 9
        elif num >= 5:
            resultado += "V"
            num -= 5
        elif num >= 4:
            resultado += "IV"
            num -= 4
        elif num >= 1:
            resultado += "I"
            num -= 1
    return resultado

# PROGRAMA PRINCIPAL
num = int(input("Ingrese un número entre el 1 y el 3999: "))
while num <= 0 or num >= 4000:
    num = int(input("Ingrese un número entre el 1 y el 3999: "))
print("Número romano:", convertirRomano(num))