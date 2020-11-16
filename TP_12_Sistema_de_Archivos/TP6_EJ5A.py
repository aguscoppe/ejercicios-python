def grabarEmpleados():
    try:
        entrada = open("TP6_EJ5A.txt", "rt")
        salida = open("TP6_EJ5A.csv", "wt")
        for linea in entrada:
            nombre = linea[:17]
            legajo = linea[17:27]
            direccion = linea[27:]
            campos = [nombre.rstrip(), legajo.rstrip(), direccion.rstrip() + "\n"]
            for i in range(len(campos) - 1):
                salida.write(campos[i] + ";")
            salida.write(campos[i+1])
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