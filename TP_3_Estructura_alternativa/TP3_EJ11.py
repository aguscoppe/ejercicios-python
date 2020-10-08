#EJERCICIO 11
year = int(input("Ingrese el año: "))
a = year % 19
b = year % 4
c = year % 7
d = ((a * 19) + 24) % 30
e = ((b * 2) + (c * 4) + (d * 6) + 5) % 7
fecha = d + e + 22

if(fecha <= 31):
    print("Pascua caerá el", fecha, "de marzo")
else:
    fecha = fecha - 31
    print("Pascua caerá el", fecha, "de abril")