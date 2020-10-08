#EJERCICIO 8
numCliente = input("Ingrese número de cliente: ")
facturaTotal = int(input("Ingrese el total de la factura: "))
descuento = (facturaTotal * 2)/100
interes = (facturaTotal * 10)/100

if(120 < descuento):
    importeDescuento = facturaTotal - 120
else:
    importeDescuento = facturaTotal - descuento
   
if(150 > interes):
    importeInteres = facturaTotal + 150
else:
    importeInteres = facturaTotal + interes

print("El precio durante los primeros 10 días del mes es de:", importeDescuento)
print("El precio entre el día 11 y 20 del mes es de:", facturaTotal)
print("El precio a partir del día 21 del mes es de:", importeInteres)