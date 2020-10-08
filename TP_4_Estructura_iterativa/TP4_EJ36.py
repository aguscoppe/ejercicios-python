# EJERCICIO 36

numLegajo = int(input("Ingrese número de legajo: "))
sueldoBasico = int(input("Ingrese sueldo básico: "))
antiguedad = int(input("Ingrese antigüedad en la empresa: "))
salario = 0

while numLegajo != 0:
    salario = sueldoBasico + ((5 * sueldoBasico) / 100) * antiguedad    
    if antiguedad > 10:
        salario = salario + ((25 * sueldoBasico) / 100)    
    print("El sueldo del empleado con legajo", numLegajo, "es de:", salario)
    numLegajo = int(input("Ingrese número de legajo: "))    
    if numLegajo > 0:
        sueldoBasico = int(input("Ingrese sueldo básico: "))
        antiguedad = int(input("Ingrese antigüedad en la empresa: "))
    else:
        print("Fin")