import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10.0  # Length of the domain
T = 5.0   # Total simulation time
Nx = 1000   # Number of spatial points
Nt = 1000  # Number of time steps
c = 1.0    # Wave speed
alpha = 0  # Linear attenuation coefficient
a = 5

# Discretization
dx = L / (Nx - 1)
dt = T / Nt

# Initial conditions
x = np.linspace(0, L, Nx)
u = np.zeros((Nx, Nt+1))
u[:, 0] = np.sin(np.pi * x / L)  # Initial displacement function (example: sine wave)

# Finite Difference Method
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u[i, n+1] = 2*(1 - alpha*dt/2)*u[i, n] - u[i, n-1] + (c*dt)**2/dx**2 * (u[i+1, n] - 2*u[i, n] + u[i-1, n]) - alpha*dt*u[i, n]

# Plot the result
plt.figure(figsize=(10, 5))
plt.imshow(u, aspect='auto', extent=[0, T, 0, L], cmap='viridis', origin='lower')
plt.colorbar(label='Amplitude')
plt.title('Wave Propagation with Attenuation')
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()

# Extract reflected wave at x = a
reflected_wave = u[int(a/dx), :]

# Plot the reflected wave
plt.figure(figsize=(8, 4))
plt.plot(np.linspace(0, T, Nt+1), reflected_wave, label='Reflected Wave')
plt.title('Reflected Wave at x = {}'.format(a))
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
