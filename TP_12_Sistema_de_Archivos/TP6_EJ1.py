def eliminarComentarios():
    try:
        entrada = open("TP6_EJ1_archivo.py", "rt")
        salida = open("TP6_EJ1_archivo_modificado.py", "wt")
        for linea in entrada:
            if linea[0] == " " and ("#" in linea or '"""' in linea):
                linea = linea.strip(" ")
            if linea[0] != "#" and linea[:3] != '"""':
                salida.write(linea)
        print("Archivo creado exitosamente")
    except FileNotFoundError as mensaje:
        print(f"No se puede abrir el archivo: {mensaje}")
    except OSError as mensaje:
        print(f"Error: {mensaje}")
    else:
        print(f"Copia finalizada")
    finally:
        try:
            entrada.close()
            salida.close()
        except NameError:
            pass
        
# PROGRAMA PRINCIPAL
eliminarComentarios()