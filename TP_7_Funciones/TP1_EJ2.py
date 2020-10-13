def ingresarFecha():
    d = int(input("Ingrese el día: "))
    m = int(input("Ingrese el mes: "))
    a = int(input("Ingrese el año: "))
    fechaValida = True
    if (d < 0 or d > 31) or (m < 0 or m > 12):
        fechaValida = False
    return fechaValida

fechaValida = ingresarFecha()
if (fechaValida):
    print("La fecha es válida")
else:
    print("La fecha es inválida")