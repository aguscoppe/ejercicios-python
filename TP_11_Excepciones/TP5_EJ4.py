def imprimirNumeros():
    n = 1
    while n <= 100000:
        try:
            print(n)
            n += 1
        except KeyboardInterrupt:
            a = input("¿Desea interrumpir el programa? (N = No) ")
            if a.upper() != "N":
                break

# PROGRAMA PRINCIPAL
imprimirNumeros()