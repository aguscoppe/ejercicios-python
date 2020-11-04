# PROGRAMA PRINCIPAL
while True:
    try:
        n = int(input("Ingrese un número natural: "))
        assert n >= 0
        break
    except ValueError:
        print("Debe ingresarse un número entero.")
    except AssertionError:
        print("El número debe ser positivo.")
    print("Intente nuevamente.")

print()
print(f"Número natural ingresado: {n}")