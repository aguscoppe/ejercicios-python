# EJERCICIO 37

numLegajo = int(input("Ingrese número de legajo: "))
categoria = int(input("Ingrese categoría del empleado: "))
salario = int(input("Ingrese salario del empleado: "))
cantEmpleados = 100
i = 1

totalSalarios = 0
masCuarenta = 0 
menosQuince = 0
sueldoAlto = salario
sueldoBajo = salario
legajoAlto = numLegajo
sueldos1 = 0
sueldos2 = 0
sueldos3 = 0

while i <= cantEmpleados:
    totalSalarios += salario
    
    if salario > 40000:
        masCuarenta += 1
    elif salario < 15000 and categoria == 3:
        menosQuince += 1
    
    if salario > sueldoAlto:
        sueldoAlto = salario
        legajoAlto = numLegajo
    elif salario < sueldoBajo:
        sueldoBajo = salario
    
    if categoria == 1:
        sueldos1 += salario
    elif categoria == 2:
        sueldos2 += salario
    else:
        sueldos3 += salario
    
    if i != cantEmpleados:
        numLegajo = int(input("Ingrese número de legajo: "))
        categoria = int(input("Ingrese categoría del empleado: "))
        salario = int(input("Ingrese salario del empleado: "))
    i += 1

print("Importe total de salarios pagados por la empresa:", totalSalarios)
print("Cantidad de empleados que ganan más de $40000:", masCuarenta)
print("Cantidad de empleados que ganan menos de $15000, cuya categoría sea 3:", menosQuince)
print("Legajo del empleado que más gana:", legajoAlto)
print("Sueldo más bajo:", sueldoBajo)
print("Importe total de sueldos categoría 1:", sueldos1)
print("Importe total de sueldos categoría 2:", sueldos2)
print("Importe total de sueldos categoría 3:", sueldos3)
print("Salario promedio:", totalSalarios / cantEmpleados)