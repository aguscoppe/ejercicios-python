# EJERCICIO 19

edad = int(input("Ingrese edad: "))
menores = 0
mayores = 0
cont = 0
totalEdad = 0

while edad != 999:
    cont = cont + 1
    totalEdad = totalEdad + edad    
    if edad < 18:
        menores = menores + 1
    else:
        mayores = mayores + 1
    edad = int(input("Ingrese edad: "))

print("El grupo tenía", menores, "menores y", mayores, "mayores de edad")
print("La edad promedio es:", totalEdad / cont)