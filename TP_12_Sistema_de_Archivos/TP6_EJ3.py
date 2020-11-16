import random

def generarAltura():
    altura = random.random() + 1
    while altura < 1.50:
        altura = random.random() + 1
    altura = str(altura)
    altura = altura[:4]
    return altura

def grabarRangoAlturas():
    generarNumero = lambda a, b: random.randint(a, b)
    cantDeportes = generarNumero(3, 10)
    cantAtletas = generarNumero(1, 10)
    try:
        arch = open("TP6_EJ3A.txt", "wt")
        for i in range(cantDeportes):
            arch.write(f"Deporte {str(i+1)}\n")
            for j in range(cantAtletas):
                altura = generarAltura()
                arch.write(f"{altura}\n")
        print(f"Archivo creado con éxito.")
    except OSError as mensaje:
        print(f"No se puede grabar el archivo: {mensaje}")
    finally:
        try:
            arch.close()
        except NameError:
            pass

def grabarPromedio():
    try:
        entrada = open("TP6_EJ3A.txt", "rt")
        salida = open("TP6_EJ3B.txt", "wt")
        alturas = []
        promedios = []
        for linea in entrada:
            try:
                altura = float(linea)
                alturas.append(altura)
            except ValueError:
                if len(alturas) > 0:
                    promedio = sum(alturas) / len(alturas)
                    promedios.append(promedio)
                    alturas = []
        promedio = sum(alturas) / len(alturas)
        promedios.append(promedio)
        for i in range(len(promedios)):
            salida.write(f"Deporte {str(i+1)}\n")
            salida.write(f"{str(promedios[i])}\n")
    except FileNotFoundError as mensaje:
        print(f"No se puede abrir el archivo: {mensaje}")
    except OSError as mensaje:
        print(f"Error: {mensaje}")
    else:
        print(f"Archivo creado con éxito.")
    finally:
        try:
            entrada.close()
            salida.close()
        except NameError:
            pass

# Media global del varón adulto: entre 1,65 a 1,8 m.
# Media global de la mujer adulta: entre 1,55 a 1,65 m.
# (1.55 + 1.80)/2
def mostrarMasAltos():
    PROMEDIO = 1.67
    try:
        arch = open("TP6_EJ3B.txt", "rt")
        for linea in arch:
            linea = linea.rstrip("\n")
            try:
                altura = float(linea)
                if altura > PROMEDIO:
                    print(f"Altura promedio del {deporte.lower()}: {altura}")
            except ValueError:
                deporte = linea
        print("Archivo leído con éxito")
    except FileNotFoundError as mensaje:
        print(f"No se puede abrir el archivo: {mensaje}")
    except OSError as mensaje:
        print(f"No se puede leer el archivo: {mensaje}")
    finally:
        try:
            arch.close()
        except NameError:
            pass

# PROGRAMA PRINCIPAL
grabarRangoAlturas()
grabarPromedio()
mostrarMasAltos()