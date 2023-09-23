import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
#|%%--%%| <kdZLdBsbf5|62y6GPCBun>

raw_data = pd.read_csv('azul.csv')
raw_data

#|%%--%%| <62y6GPCBun|DoRISqZKKP>

I_D = raw_data['I_D']
V_D = raw_data['V_D']

#|%%--%%| <DoRISqZKKP|cB2KzCcNzf>

y = I_D.copy()#/max(I_D)
x = V_D.copy()#/max(V_D)

plt.scatter(x,y)
plt.xlabel(f'$V_D (V)$', color = "black")
plt.ylabel(f'$I_D (A)$', color = "black")
plt.title(f'Voltaje vs Corriente con $\lambda = 6.15x10^{{-7}}$', color = "black")
plt.grid()

#Voltaje umbral 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x[14:],y[14:])
a,b = coef
print(f'coef. lineal: {coef}')

xx = np.linspace(2.54,2.97,18)
yy = reg_func(xx,a,b)

residuals = y[12:] - reg_func(x[12:],a,b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)

plt.plot(xx,yy,c="green", label = f"$I_L = ({a:.2f}±{0.01:.2f})*V_L + ({b:.2f}±{0.02:.2f}), R^2 = {r_squared:.2f}$")

reg_func_inv = lambda y,a,b: (y-b)/a
V_U = reg_func_inv(0,a,b)
print(f'V_U = {V_U:.2f}')

plt.scatter([V_U],[0],c='magenta', label = f'$V_U = ({V_U:.2f}\pm 0.2) V$')

l = 5.6e-7
c = 2.9e8
q = 1.6e-19

h = q*V_U*l/c

print(f'h = {h}')

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'
plt.savefig('V_DvsI_D.jpg')

