n = int(input("Ingrese un número entero positivo: "))
cantTerminos = 1

if n <= 0:
    print("Error: el número debe ser positivo")
else:    
    while n != 1:
        print(n)
        cantTerminos += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1

    print(n)
    print("La cantidad de términos obtenidos es:", cantTerminos)