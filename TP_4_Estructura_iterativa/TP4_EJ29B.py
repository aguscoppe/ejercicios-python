# EJERCICIO 29 - Versión B

s = int(input("Ingrese la cantidad de semanas: "))
i = 0
erores = 0

# multiplicamos s * 2 para que cada vuelta de ciclo
# represente un programa en lugar de una semana
while i < (s*2):
    errores = 2**i
    i += 1

print("Juancito cometió", errores, "errores en su último programa")