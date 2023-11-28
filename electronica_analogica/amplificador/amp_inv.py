import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
#imports para la regresion 
from scipy.optimize import curve_fit

raw_data = pd.read_csv("amplificador_no_inv_region_lineal.csv")

print(raw_data)

x = raw_data['V_i'] 
y = raw_data['V_0'] 

plt.scatter(x,y)

reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x[5:18],y[5:18])
a,b = coef

xx = x[5:18]
yy = reg_func(xx,a,b)

plt.plot(xx,yy,c="green", label=f'y = x({a:.2f})+{b:.2f}')

plt.xlabel(f'$V_i$')
plt.ylabel(f'$V_0$')
plt.grid()
plt.show()
