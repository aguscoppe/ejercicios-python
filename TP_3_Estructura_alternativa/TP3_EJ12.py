#EJERCICIO 12
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
ano = int(input("Ingrese el año: "))

# asignación de cadena de caracteres a dos variables
# para evitar código repetitivo
fechaCorrecta = "La fecha es válida"
fechaIncorrecta = "La fecha no es válida"

if mes > 12 or mes <= 0 or ano <= 0 or dia > 31 or dia <= 0:
    print(fechaIncorrecta)
# verificación febrero + año bisiesto
# en otro contexto le correspondería su propio módulo
elif (dia == 29 and mes == 2):
    if (ano % 400) == 0:
        print(fechaCorrecta)
    elif (ano % 100) == 0:
        print(fechaIncorrecta)
    elif (ano % 4) == 0:
        print(fechaCorrecta)
    else:
        print(fechaIncorrecta)
elif dia <= 28 and mes == 2:
    print(fechaCorrecta)
# verificación meses de 30 días
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia < 31:
        print(fechaCorrecta)
    else:
        print(fechaIncorrecta)
# verificación meses de 31 días
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        print(fechaCorrecta)
    else:
        print(fechaIncorrecta)
else:
    print(fechaIncorrecta)