import rawpy
import numpy as np
import os
import matplotlib.pyplot as plt

def colores(name):
    # Abre la imagen DNG
    with rawpy.imread(f"{name}") as raw:
        # Obtiene la matriz de píxeles raw
        raw_array = raw.postprocess()

    # Extrae las matrices de valores RGB
    red_channel = raw_array[:, :, 0]
    green_channel = raw_array[:, :, 1]
    blue_channel = raw_array[:, :, 2]

    # Coordenadas del punto específico (cambia estas coordenadas)
    x, y = 1660, 1330
    #x, y = 1530, 1145

    # Tamaño del cuadrado para el promedio
    square_size = 30

    # Calcula el promedio de los puntos adyacentes en el cuadrado
    if (x - square_size // 2) >= 0 and (y - square_size // 2) >= 0:
        submatrix_red = red_channel[y - square_size // 2:y + square_size // 2, x - square_size // 2:x + square_size // 2]
        submatrix_green = green_channel[y - square_size // 2:y + square_size // 2, x - square_size // 2:x + square_size // 2]
        submatrix_blue = blue_channel[y - square_size // 2:y + square_size // 2, x - square_size // 2:x + square_size // 2]

        # Calcula el promedio de cada canal
        avg_red = np.mean(submatrix_red)
        avg_green = np.mean(submatrix_green)
        avg_blue = np.mean(submatrix_blue)

        print("Promedio de los puntos adyacentes (RGB):")
        print(f"Red: {avg_red}")
        print(f"Green: {avg_green}")
        print(f"Blue: {avg_blue}")
        return avg_red,avg_green,avg_blue
    else:
        print("El punto especificado se encuentra muy cerca del borde de la imagen. Asegúrate de que esté lo suficientemente alejado para aplicar el cuadrado de 30x30 píxeles.")
        return 0, 0,0

# Carpeta actual donde se ejecuta el script
current_directory = os.getcwd()

# Lista para almacenar nombres de archivos .dng
dng_files = []

# Recorre los archivos en la carpeta actual
for filename in os.listdir(current_directory):
    if filename.endswith(".dng"):
        dng_files.append(filename)

# Ordena los archivos por fecha de modificación (el más antiguo primero)
dng_files.sort(key=lambda x: os.path.getmtime(x))
print(dng_files)
degree = 0

# RGB por grado
r_list = {}
g_list = {}
b_list = {}

# Procesa cada imagen
for dng_file in dng_files:
    image_path = os.path.join(current_directory, dng_file)
    print(f'{degree}: \n')
    r,g,b = colores(image_path)  # Llama a tu función colores con la imagen
    r_list[degree] = r
    g_list[degree] = g
    b_list[degree] = b
    degree +=10
    print('\n')
print(r_list)

def plotear(data,color,n):
    # Convertir los ángulos de grados a radianes
    angles = np.deg2rad(list(data.keys()))
    radii = list(data.values())

    # Crear un gráfico polar
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Dibuja los datos en el gráfico polar
    ax.plot(angles, radii, marker='o',c = color)

    # Asegura que el gráfico abarque de 0 a 360 grados y de 0 a 255 en los radios
    ax.set_thetamin(0)
    ax.set_thetamax(360)
    ax.set_ylim(0, 255)

    # Título
    plt.title(f"{n}")

    # Mostrar el gráfico
    plt.show()

plotear(r_list,'red','Rojo')
plotear(g_list,'green','Verde')
plotear(b_list,'blue','Azul')
