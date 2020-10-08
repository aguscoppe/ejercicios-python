#EJERCICIO 8

numVen = int(input("Ingrese número de vendedor "))
ventas = int(input("Ingrese número de ventas "))
totalVentas = int(input("Ingrese el valor total de las ventas "))
sue = 800 + (ventas*50) + ((totalVentas*5)/100)
print("Al vendedor", numVen, "le corresponde un sueldo de", sue, "pesos")