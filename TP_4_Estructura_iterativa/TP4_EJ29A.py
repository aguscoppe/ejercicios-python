# EJERCICIO 29 - Versión A

s = int(input("Ingrese la cantidad de semanas: "))
i = 1
errores = 1

# incrementamos i en 0.5 porque se realizan dos programas por semana
while i <= s:
    errores = errores * 2
    i += 0.5

print("Juancito cometió", errores, "errores en su último programa")