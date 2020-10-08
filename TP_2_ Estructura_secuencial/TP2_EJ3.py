#EJERCICIO 3

r = int(input("Ingresar la longitud del radio de un círculo "))
pi = 355/113
supCir = pi * (r**2)
per = pi * (r*2)
supEs = 4 * pi * (r**2)
vol = 4/3 * pi * (r**3)
print("Superficie del círculo:", supCir)
print("Perímetro de la circunferencia:", per)
print("Superficie de la esfera:", supEs)
print("Volumen de la esfera:", vol)