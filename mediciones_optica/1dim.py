import numpy as np
import matplotlib.pyplot as plt

# Parámetros del tubo
longitud_tubo = 1.0  # metros
diametro_tubo = 0.15  # metros
radio_tubo = diametro_tubo / 2

# Parámetros de la simulación
tiempo_simulacion = 0.02  # segundos
velocidad_sonido = 343.0  # velocidad del sonido en el aire a 20°C en m/s
frecuencia_inicial = 440.0  # frecuencia inicial de la onda

# Crear el espacio de simulación en el eje x
x = np.linspace(0, longitud_tubo, 1000)

# Crear el espacio de simulación en el tiempo
t = np.linspace(0, tiempo_simulacion, 1000)

# Calcular la onda acústica
frecuencia_angular = 2 * np.pi * frecuencia_inicial
onda_acustica = np.sin(frecuencia_angular * t) * np.sin(np.pi * x / longitud_tubo)

# Visualizar la onda acústica en el tubo
plt.plot(x, onda_acustica)
plt.title('Simulación de Onda Acústica en un Tubo Cilíndrico')
plt.xlabel('Posición en el Tubo (m)')
plt.ylabel('Amplitud de la Onda')
plt.show()
