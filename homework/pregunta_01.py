"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def pregunta_01():
    
    # leer el archivo de texto
    with open("files/input/clusters_report.txt") as archivo:
        lineas = archivo.readlines()

    # filtrar líneas, eliminando aquellas con "---"
    lineas_limpias = []
    for linea in lineas:
        if "---" not in linea:
            lineas_limpias.append(linea.strip())

    # extraer y procesar encabezados
    encabezados = re.split(r"\s{2,}", lineas_limpias[0])
    encabezados[1] += " palabras clave"
    encabezados[2] += " palabras clave"

    # procesar los datos
    datos_procesados = []
    fila_temporal = encabezados 

    for linea in lineas_limpias[2:]:
        elementos = re.split(r"\s{2,}", linea)

        if len(linea) == 0:
            continue

        if elementos[0].isdigit():
            # guardar la fila anterior antes de comenzar una nueva
            datos_procesados.append(fila_temporal)
            fila_temporal = []
            fila_temporal.append(int(elementos[0]))  
            fila_temporal.append(int(elementos[1]))
            fila_temporal.append(float(elementos[2].split()[0].replace(',', '.'))) 

            # extraer la descripción de palabras clave
            indice_porcentaje = linea.find("%")
            palabras_clave = re.sub(r'\s+', ' ', linea[indice_porcentaje + 1:].strip())
            fila_temporal.append(palabras_clave)
        else:
            # continuar con la descripción de palabras clave
            texto_limpio = re.sub(r'\s+', ' ', linea.strip()).replace(".", "")
            fila_temporal[-1] += " " + texto_limpio.strip()

    datos_procesados.append(fila_temporal)

    
    datos_procesados[0] = [nombre.lower().replace(" ", "_") for nombre in datos_procesados[0]]

    
    dataframe_final = pd.DataFrame(data=datos_procesados[1:], columns=datos_procesados[0])

    return dataframe_final

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """