a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

multiplos = [i for i in range(a, b) if i % 7 == 0 and i % 5 != 0]

print(multiplos)