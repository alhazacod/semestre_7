import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
from scipy.optimize import fsolve
#Para hallar el maximo de una funcion 
from scipy.optimize import minimize_scalar
#|%%--%%| <bmd0FicXQm|iM1cI3Iry8>

raw_data = pd.read_csv("datos_rlc.csv")

print(raw_data)

x = raw_data['Frecuencia (kHz)']
x = x/max(x)
y = raw_data['Voltaje (mV)']
y = y/max(y)
print(f'max x: {max(raw_data["Frecuencia (kHz)"])}, max y: {max(raw_data["Voltaje (mV)"])}')
#|%%--%%| <iM1cI3Iry8|2VnEcwgl43>

plt.scatter(x*60,y*1600)
plt.grid()
plt.xlabel('Frecuencia (kHz)')
plt.ylabel('Voltaje (mV)')
plt.title('Voltaje vs Frecuencia')

#Realizamos la regresion 
reg_func = lambda x,a,b,c: x/(a*x**2+b*x+c)
coef,cov = curve_fit(reg_func, x,y, p0 = [113,-114,29])
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b,c = (113.12,-114.85,29.67)


xx = np.linspace(0.415,0.63,50)
yy = reg_func(xx,a,b,c)

# Graficamos la regresion lineal 
plt.plot(xx*60,yy*1600,c="green")

# Encontramos el punto maximo
maximo = minimize_scalar(lambda x: -reg_func(x,a,b,c), method='bounded', bounds=(0, 1))

plt.scatter([maximo.x*60],[-maximo.fun*1600],c="magenta", marker = '^', s=120, label = f'Punto Maximo ({maximo.x*60:.2f},{-maximo.fun*1600:.2f})')

print(f'Punto Maximo ({maximo.x*60:.2f},{-maximo.fun*1600:.2f})')

print(f'70%: {-maximo.fun*0.7*60}')

#|%%--%%| <2VnEcwgl43|dvPQV7IR8e>

paso = 1e-4
x = np.arange(0,1,paso)
cortes = []

for i in x:
    diff = abs(reg_func(i,a,b,c) - (-maximo.fun*0.7))
    if diff<0.0005:
        print(f'{i*60}')
        cortes.append(i)
