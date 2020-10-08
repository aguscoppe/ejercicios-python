sueldoBasico = int(input("Ingrese sueldo básico del empleado: "))
antiguedad = int(input("Ingrese antigüedad del empleado: "))
estadoCivil = input("Ingrese estado civil del empleado (S/C): ")
sueldoBruto = 0
sueldoNeto = 0
jubilacion = (sueldoBasico * 11)/100
obraSocial = (sueldoBasico * 3)/100
sindicato = (sueldoBasico * 3)/100

if estadoCivil == "s":
    sueldoBruto = sueldoBasico + ((sueldoBasico * 5)/100) * antiguedad
    print("Estado civil: soltero")
else:
    sueldoBruto = sueldoBasico + ((sueldoBasico * 7)/100) * antiguedad
    print("Estado civil: casado")

sueldoNeto = sueldoBruto - jubilacion - obraSocial - sindicato
print("Antigüedad:", antiguedad, "años")
print("Sueldo bruto:", sueldoBruto)
print("Descuentos -> Jubilación:", jubilacion, "| Obra social:", obraSocial, "| Sindicato:", sindicato)
print("Sueldo neto:", sueldoNeto)