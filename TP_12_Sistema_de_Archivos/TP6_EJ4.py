def grabarApellidos():
    try:
        entrada = open("TP6_EJ4.txt", "rt")
        armenia = open("TP6_EJ4_ARMENIA.txt", "wt")
        italia = open("TP6_EJ4_ITALIA.txt", "wt")
        españa = open("TP6_EJ4_ESPAÑA.txt", "wt")
        for linea in entrada:
            apellido, nombre = linea.split(", ")
            longitud = len(apellido)
            apellido = apellido[longitud-3:].lower()
            if apellido == "ian":
                armenia.write(linea)
            elif apellido == "ini":
                italia.write(linea)
            elif apellido[1:] == "ez":
                españa.write(linea)
    except FileNotFoundError as mensaje:
        print(f"No se puede abrir el archivo: {mensaje}")
    except OSError as mensaje:
        print(f"Error: {mensaje}")
    else:
        print(f"Archivo creado con éxito.")
    finally:
        try:
            entrada.close()
            armenia.close()
            italia.close()
            españa.close()
        except NameError:
            pass

# PROGRAMA PRINCIPAL
grabarApellidos()