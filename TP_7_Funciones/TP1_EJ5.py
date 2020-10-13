def imprimirPatronFijo(filas):
    print("---Patrón fijo---")
    for i in range(filas):
        print("**********")

def imprimirPatronDinamico(filas):
    print("---Patrón dinámico---")
    total = ""
    for i in range(filas):
        total += "**"
        print(total)

f = int(input("Ingrese la cantidad de filas: "))
imprimirPatronFijo(f)
imprimirPatronDinamico(f)