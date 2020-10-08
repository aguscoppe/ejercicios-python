#EJERCICIO 9
year = int(input("Ingrese el año: "))
if (year % 400) == 0:
    print("El año", year, "es bisiesto")
elif (year % 100) == 0:
    print("El año", year, "no es bisiesto")
elif (year % 4) == 0:
    print("El año", year, "es bisiesto")
else:
    print("El año", year, "no es bisiesto")