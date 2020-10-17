def filtrarPalabras(n, cadena):
    palabras = cadena.split()
    nueva = ""
    for palabra in palabras:
        if len(palabra) >= n:
            nueva = nueva + palabra + " "
    return nueva

# PROGRAMA PRINCIPAL
frase = '''En un lugar de la Mancha de cuyo nombre no quiero acordarme
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero
adarga antigua rocín flaco y galgo corredor'''
n = int(input("Ingrese un número entero: "))

print("Palabras cuya longitud es mayor o igual a",
      n, "-", filtrarPalabras(n, frase))