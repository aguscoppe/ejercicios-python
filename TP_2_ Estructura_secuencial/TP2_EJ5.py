#EJERCICIO 5

metro = float(input("Ingrese una medida en metros "))
cent = metro*100
pulg = cent/2.54
pie = pulg/12
yar = pie/3
print(metro, "metros equivalen a", cent, "cm")
print(metro, "metros equivalen a", pulg, "pulgadas")
print(metro, "metros equivalen a", pie, "pies")
print(metro, "metros equivalen a", yar, "yardas")