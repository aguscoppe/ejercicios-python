c = input("Ingrese una palabra: ")
espacio = " "
espacios = (80 - len(c))//2

print()
print(espacio * espacios + c + espacio * espacios)