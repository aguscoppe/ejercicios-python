#EJERCICIO 9
totalDinero = int(input("Ingrese la cantidad total de dinero: "))
aux = totalDinero

cant100 = totalDinero // 100
aux = totalDinero % 100
cant50 = aux // 50
aux = aux % 50
cant10 = aux // 10
aux = aux % 10
cant5 = aux // 5
cant1 = aux % 5
print("Dinero total:", totalDinero)
print("Billetes:", cant100, "de $100,", cant50, "de $50,", cant10, "de $10,", cant5, "de $5 y", cant1, "de $1")