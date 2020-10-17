frase = '''En un lugar de la Mancha de cuyo nombre no quiero acordarme
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero
adarga antigua rocín flaco y galgo corredor'''

n = int(input("Ingrese un número entero: "))

p = frase.split()

palabras = list(filter(lambda p: len(p) >= n, p))

nuevaCadena = ", ".join(palabras)

print(nuevaCadena)