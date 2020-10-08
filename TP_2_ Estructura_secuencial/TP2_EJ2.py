#EJERCICIO 3

import math

r = int(input("Ingresar la longitud del radio de un círculo "))
supCir = math.pi * (r**2)
per = math.pi * (r*2)
supEs = 4 * math.pi * (r**2)
vol = 4/3 * math.pi * (r**3)
print("Superficie del círculo:", supCir)
print("Perímetro de la circunferencia:", per)
print("Superficie de la esfera:", supEs)
print("Volumen de la esfera:", vol)