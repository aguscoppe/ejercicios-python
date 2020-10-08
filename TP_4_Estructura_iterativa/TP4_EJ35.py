# EJERCICIO 35

productoA = int(input("Indique si acepta el producto A (0 = No | 1 = Sí): "))
productoB = int(input("Indique si acepta el producto B (0 = No | 1 = Sí): "))
totalClientes = 100
i = 0
totalA = 0
totalB = 0
totalSoloA = 0
totalSoloB = 0
totalAB = 0
totalNo = 0

while i < totalClientes:
    if productoA == 1:
        totalA += 1
    if productoB == 1:
        totalB += 1
    if productoA == 1 and productoB == 0:
        totalSoloA += 1
    elif productoA == 0 and productoB == 1:
        totalSoloB += 1
    elif productoB == 0 and productoA == 0:
        totalAB += 1
    elif productoB == 1 and productoA == 1:
        totalNo += 1
    i += 1
    if i != totalClientes:
        productoA = int(input("Indique si acepta el producto A (0 = No | 1 = Sí): "))
        productoB = int(input("Indique si acepta el producto B (0 = No | 1 = Sí): "))

totalA = (totalA * 100) / totalClientes
totalB = (totalB * 100) / totalClientes
totalSoloA = (totalSoloA * 100) / totalClientes
totalSoloB = (totalSoloB * 100) / totalClientes
totalAB = (totalAB * 100) / totalClientes
totalNo = (totalNo * 100) / totalClientes

print("Porcentaje que aprobó el producto A:", totalA)
print("Porcentaje que aprobó el producto B:", totalB)
print("Porcentaje que solamente aprobó el producto A:", totalSoloA)
print("Porcentaje que solamente aprobó el producto B:", totalSoloB)
print("Porcentaje que no aprobó ningún producto:", totalAB)
print("Porcentaje que aprobó ambos productos:", totalNo)