def devolverMes(mes):
    meses = ["enero", "febrero", "marzo", "abril",
             "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre",
             "diciembre"]
    try:
        assert 1 <= mes <= 12
        mes = meses[mes-1]
    except AssertionError:
        mes = ""
    return mes

# PROGRAMA PRINCIPAL
while True:
    try:
        n = int(input("Ingrese un número del 1 al 12: "))
        break
    except ValueError:
        print("Debe ingresarse un número entero.")
print()
res = devolverMes(n)
print(f"El mes {n} es: {res}")