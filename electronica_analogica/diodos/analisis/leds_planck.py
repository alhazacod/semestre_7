import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
#|%%--%%| <kdZLdBsbf5|62y6GPCBun>
name = 'rojo'
raw_data = pd.read_csv(f'{name}.csv')
raw_data

#|%%--%%| <62y6GPCBun|DoRISqZKKP>

I_D = raw_data['I_D']
V_D = raw_data['V_D']

#|%%--%%| <DoRISqZKKP|cB2KzCcNzf>
l = 6.7e-7

y = I_D.copy()#/max(I_D)
x = V_D.copy()#/max(V_D)

plt.scatter(x,y)
plt.xlabel(f'$V_D (V)$', color = "black")
plt.ylabel(f'$I_D (A)$', color = "black")
plt.title(f'Voltaje vs Corriente con $\lambda = {l}$', color = "black")
plt.grid()

#Voltaje umbral 
inicio = 13
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x[inicio:],y[inicio:])
a,b = coef
print(f'coef. lineal: {coef}')

xx = x[12:]
yy = reg_func(xx,a,b)

residuals = y[inicio:] - reg_func(x[inicio:],a,b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)

plt.plot(xx,yy,c="green", label = f"$I_L = ({a:.2f}±{0.01:.2f})*V_L + ({b:.2f}±{0.02:.2f}), R^2 = {r_squared:.2f}$")

reg_func_inv = lambda y,a,b: (y-b)/a
V_U = reg_func_inv(0,a,b)
print(f'V_U = {V_U:.2f}')

plt.scatter([V_U],[0],c='magenta', label = f'$V_U = ({V_U:.2f}\pm 0.2) V$')

c = 2.9e8
q = 1.6e-19

h = q*V_U*l/c

print(f'h = {h}')

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'
plt.savefig(f'{name}.jpg')

