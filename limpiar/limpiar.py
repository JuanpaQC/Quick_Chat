import os
import time

def limpiar_archivo_txt(ruta_entrada, ruta_salida):
    """
    Limpia un archivo de texto eliminando espacios en blanco al principio y al final de cada línea,
    convirtiendo todo a minúsculas y eliminando caracteres especiales. Además, guarda el archivo con
    codificación UTF-8.

    :param ruta_entrada: Ruta del archivo de texto a limpiar.
    :param ruta_salida: Ruta donde se guardará el archivo limpio.
    """
    # Asegúrate de que la ruta de salida incluya el nombre del archivo
    nombre_archivo_salida = "mensajes_limpios.txt"
    ruta_completa_salida = os.path.join(ruta_salida, nombre_archivo_salida)
    
    while True:
        # Abre el archivo de entrada en modo lectura y el de salida en modo escritura con codificación UTF-8
        with open(ruta_entrada, 'r', encoding='utf-8') as archivo_entrada, \
             open(ruta_completa_salida, 'w', encoding='utf-8') as archivo_salida:
            
            # Lee cada línea del archivo de entrada
            for linea in archivo_entrada:
                # Elimina espacios en blanco al principio y al final de la línea
                linea = linea.strip()
                
                # Convierte la línea a minúsculas
                linea = linea.lower()
                
                # Elimina caracteres especiales (puedes ajustar esta expresión según tus necesidades)
                linea = ''.join(e for e in linea if e.isalnum() or e.isspace())
                
                # Escribe la línea limpia en el archivo de salida
                archivo_salida.write(linea + '\n')

        # Espera un tiempo antes de volver a verificar el archivo de entrada
        time.sleep(1)  # Ajusta el tiempo de espera según tus necesidades

# Ejemplo de uso
ruta_entrada = "C:\\Users\\jpqca\\Downloads\\TestMASM\\TestMASM\\mensajes.txt"
ruta_salida = "C:\\Users\\jpqca\\Downloads\\TestMASM\\TestMASM"
limpiar_archivo_txt(ruta_entrada, ruta_salida)
