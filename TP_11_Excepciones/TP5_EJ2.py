def sumarCadenas(cad1, cad2):
    try:
        cad1 = float(cad1)
        cad2 = float(cad2)
        res = cad1 + cad2
    except ValueError:
        res = -1
    return res 

# PROGRAMA PRINCIPAL
a = input("Ingrese un número real: ")
b = input("Ingrese otro número real: ")

print()
res = sumarCadenas(a, b)
print(res)