import os
import pandas as pd
import matplotlib.pyplot as plt

def leer_archivos_csv_en_carpeta(carpeta):
    datos_diccionario = {}
    
    # Obtener la lista de archivos en la carpeta
    archivos_csv = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.csv')]
    
    for archivo_csv in archivos_csv:
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta, archivo_csv)
        
        # Leer el archivo CSV utilizando pandas
        datos = pd.read_csv(ruta_archivo)
        
        # Almacenar los datos en el diccionario usando el nombre del archivo como clave
        datos_diccionario[archivo_csv] = datos
    
    return datos_diccionario

def graficar_scatter(diccionario_datos):
        
    # Iterar a través del diccionario y graficar los datos de cada archivo
    for nombre_archivo, datos in diccionario_datos.items():
        # Utilizar scatter plot para graficar los datos de cada archivo
        plt.scatter(datos['V_CE'], datos['I_C'], label=nombre_archivo[:-4])  # Elimina la extensión ".csv" del nombre
        

def graficar_plot(diccionario_datos):
        
    # Iterar a través del diccionario y graficar los datos de cada archivo
    for nombre_archivo, datos in diccionario_datos.items():
        # Utilizar scatter plot para graficar los datos de cada archivo
        plt.plot(datos['V_CE'], datos['I_C'], label=nombre_archivo[:-4])  # Elimina la extensión ".csv" del nombre


# Llama a la función para leer los archivos CSV en la carpeta especificada
data = leer_archivos_csv_en_carpeta('datos')
linea_carga = leer_archivos_csv_en_carpeta('linea_carga')

# Crear una nueva figura
plt.figure(figsize=(10, 6))

graficar_scatter(data)
graficar_plot(linea_carga)

# Agregar etiquetas y título
plt.xlabel('V_CE')
plt.ylabel('I_C')

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
