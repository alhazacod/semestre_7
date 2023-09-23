import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
#|%%--%%| <pgLtdGpmhG|MpOeI3w5y2>

raw_data = pd.read_csv('temperatura_diodo_zener.csv')
raw_data

#|%%--%%| <MpOeI3w5y2|KCnslOJRwx>

x = raw_data['T']
y = raw_data['V_z']

plt.scatter(x,y)
plt.xlabel(f'$T (K)$', color = "black")
plt.ylabel(f'$V_z (V)$', color = "black")
plt.title('Voltaje zener vs Temperatura', color = "black")
plt.grid()

#Voltaje umbral 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x,y)
a,b = coef
print(f'coef. lineal: {coef}')

xx = np.linspace(125,360,50)
yy = reg_func(xx,a,b)

residuals = y - reg_func(x,a,b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)

plt.plot(xx,yy,c="green", label = f"$V_z = ({a:.3f}±{0.003:.3f})*T + ({b:.3f}±{0.005:.3f}), R^2 = {r_squared:.2f}$")

plt.legend()

plt.rcParams['axes.facecolor'] = 'white'
plt.savefig('V_zvsT.jpg')

