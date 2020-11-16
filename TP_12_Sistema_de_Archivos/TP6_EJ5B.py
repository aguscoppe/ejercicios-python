def grabarEmpleados():
    try:
        entrada = open("TP6_EJ5B.txt", "rt")
        salida = open("TP6_EJ5B.csv", "wt")
        for linea in entrada:
            nombre, legajo, direccion = linea.split("#")
            campos = [nombre, legajo, direccion]
            for i in range(len(campos) - 1):
                salida.write(f"{campos[i]};")
            salida.write(f"{campos[i+1]}")
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

# PROGRAMA PRINCIPAL
grabarEmpleados()