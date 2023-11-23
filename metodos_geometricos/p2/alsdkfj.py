import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la función que representa el sistema de ecuaciones diferenciales
def sistema_ecuaciones(y, t, a):
    r, v = y
    drdt = v
    dvdt = a * abs(v) / abs(r)**2
    return [drdt, dvdt]

# Condiciones iniciales
r0 = 1.0  # Cambia según tus necesidades
v0 = 1.0  # Cambia según tus necesidades
condiciones_iniciales = [r0, v0]

# Parámetro 'a'
a = 1.0*np.sin(np.pi/4)  # Cambia según tus necesidades

# Tiempo de integración
t = np.linspace(0, 10, 1000)  # Cambia según tus necesidades

# Resolver el sistema de ecuaciones diferenciales
solucion = odeint(sistema_ecuaciones, condiciones_iniciales, t, args=(a,))

# Graficar la solución
plt.figure(figsize=(10, 5))
plt.plot(t, solucion[:, 0], label='r(t)')
plt.plot(t, solucion[:, 1], label='v(t)')
plt.xlabel('Tiempo')
plt.ylabel('Solución')
plt.legend()
plt.show()
