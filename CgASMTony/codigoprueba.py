def agregar_contenido_a_archivo(ruta_archivo, contenido):
    try:
        with open(ruta_archivo, 'a') as archivo:
            archivo.write(contenido + '\n')  # Agrega el contenido en una nueva línea
        print("Contenido agregado exitosamente al archivo.")
    except Exception as e:
        print(f"Ocurrió un error al intentar agregar contenido al archivo: {e}")

ruta_archivo = r"C:\Users\Armando Huertas\Desktop\CgASMTony\msj.txt"

contenido_a_agregar = input("Ingrese el contenido que desea agregar al archivo: ")

agregar_contenido_a_archivo(ruta_archivo, contenido_a_agregar)
