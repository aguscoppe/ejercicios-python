#EJERCICIO 6
paginas = int(input("Ingrese cantidad de páginas: "))
costoBasico = 125
costoTotal = costoBasico + (paginas*2.2)
if paginas > 300 and paginas <= 600:
    costoTotal = costoTotal + 80
elif paginas > 600:
    costoTotal = costoTotal + 136
print("El costo total de un libro de", paginas, "páginas es de", costoTotal, "pesos")