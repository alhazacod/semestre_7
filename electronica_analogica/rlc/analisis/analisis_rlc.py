import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
from scipy.optimize import fsolve
#Para hallar el maximo de una funcion 
from scipy.optimize import minimize_scalar
#|%%--%%| <bmd0FicXQm|dvPQV7IR8e>

def punto_corte(corte,func):
    paso = 1e-4
    rango = np.arange(0,1,paso)
    cortes = []

    for i in rango:
        diff = abs(func(i) - (corte*0.7))
        if diff<0.0005:
            cortes.append(i*60)
    return cortes

#|%%--%%| <dvPQV7IR8e|iM1cI3Iry8>

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
plt.xlabel('Frecuencia (kHz)', color = 'black')
plt.ylabel('Voltaje (mV)', color = 'black')
plt.title('Voltaje vs Frecuencia', color = 'black')

#Realizamos la regresion 
reg_func = lambda x,a,b,c: x/(a*x**2+b*x+c)
coef,cov = curve_fit(reg_func, x,y, p0 = [113,-114,29])
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b,c = (113.12,-114.85,29.67)


xx = np.linspace(0.415,0.63,50)
yy = reg_func(xx,a,b,c)

# Graficamos la regresion  
plt.plot(xx*60,yy*1600,c="green",label='Linea de tendencia')

# Encontramos el punto maximo
maximo = minimize_scalar(lambda x: -reg_func(x,a,b,c), method='bounded', bounds=(0, 1))

print(f'Punto Maximo ({maximo.x*60:.2f},{-maximo.fun*1600:.2f})')

print(f'70%: {-maximo.fun*0.7*60}')
print(f'130%: {-maximo.fun*1.3*60}')

puntos_corte = punto_corte(-maximo.fun,lambda x: reg_func(x,a,b,c))
print(f'Puntos de corte: {puntos_corte}')

plt.scatter([maximo.x*60],[-maximo.fun*1600],c="magenta", marker = '^', s=120, label = f'Punto Maximo ({maximo.x*60:.2f},{-maximo.fun*1600:.2f})')
plt.vlines(x = puntos_corte, color = 'r', ymin = 0, ymax = max(y*1600),linestyles = '--', alpha = 0.4, label = f'BW = {puntos_corte[1]-puntos_corte[0]: .2f}kHz')
plt.legend(loc='center left')
plt.rcParams['axes.facecolor'] = 'white'
#plt.savefig('v_f.jpg')
#plt.close()
#|%%--%%| <2VnEcwgl43|Tmb2Mqjh6Y>

#Diagrama de bode
x = raw_data['Frecuencia (kHz)']
y = raw_data['Voltaje (mV)']

v_out = y
v_in = 5 #[V]
A_v = 20 * np.log10(v_out/v_in)

x = np.log(x) 
y = A_v 

#Graficamos los datos
plt.scatter(x,y)
plt.grid()
plt.xlabel('Ln(Frecuencia)', color = 'black')
plt.ylabel('20 Log10(V_out/V_in)', color = 'black')
plt.title('Diagrama de Bode', color = 'black')


#antes del pico 
x_bode_b = x[:10]
y_bode_b = y[:10]

#Realizamos la regresion 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x_bode_b,y_bode_b)
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b = coef


xx = np.linspace(0,3.2,50)
yy = reg_func(xx,a,b)

# Graficamos la regresion  
plt.plot(xx,yy,c="green",label=f'y = x*({a:.2f})+{b:.2f}')

#despues del pico 
x_bode_a = x[24:]
y_bode_a = y[24:]

#Realizamos la regresion 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x_bode_a,y_bode_a)
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b = coef


xx = np.linspace(3.6,4.1,50)
yy = reg_func(xx,a,b)

# Graficamos la regresion  
plt.plot(xx,yy,c="orange",label=f'y =x*({a:.2f})+{b:.2f}')

plt.legend()

plt.savefig('dobe.jpg')
