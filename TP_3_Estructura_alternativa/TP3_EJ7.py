# EJERCICIO 7
cantidad = int(input("Indique la cantidad solicitada del producto: "))
precioBase = int(input("Indique el precio base de dicho producto: "))
promedio = 0
aux = cantidad
precioTotal = cantidad * precioBase
aux = aux - 12

if aux >= 1:
    precioTotal = precioTotal - (aux * ((precioBase*10)/100))
    aux = cantidad - 100

if aux >= 1:
    precioTotal = precioTotal - (aux * ((precioBase*15)/100))

promedio = precioTotal / cantidad
print("El precio total de", cantidad, "productos es de", precioTotal, "pesos. Su valor promedio es de:", promedio, "pesos")