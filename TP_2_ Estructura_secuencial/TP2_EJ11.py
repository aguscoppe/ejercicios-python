#EJERCICIO 11

binario = int(input("Ingrese un número binario de 4 cifras: "))
uno = (binario % 10) * (2**0)
diez = ((binario // 10) % 10) * (2**1)
cien = (((binario // 10) //10) % 10) * (2**2)
mil = ((((binario // 10) // 10) // 10) % 10) * (2**3)
resultado = uno + diez + cien + mil
print("El número equivale a", resultado)