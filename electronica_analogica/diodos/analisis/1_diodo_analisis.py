import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
#|%%--%%| <S7D56Q76gG|L4ZV5NsvOM>

raw_data = pd.read_csv('1_diodo.csv')
raw_data
#|%%--%%| <L4ZV5NsvOM|pG1ifQWwyd>

I_D = raw_data['I_D']
V_D = raw_data['V_D']

#|%%--%%| <pG1ifQWwyd|JXNE6eQZQO>

y = I_D.copy()#/max(I_D)
x = V_D.copy()#/max(V_D)

plt.scatter(x,y)
plt.xlabel(f'$V_D (V)$', color = "black")
plt.ylabel(f'$I_D (A)$', color = "black")
plt.title('Voltaje vs Corriente de carga', color = "black")
plt.grid()

#Voltaje umbral 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x[19:],y[19:])
a,b = coef
print(coef)

xx = np.linspace(0.685,0.75,50)
yy = reg_func(xx,a,b)

plt.plot(xx,yy,c="green")

reg_func_inv = lambda y,a,b: (y-b)/a
V_U = reg_func_inv(0,a,b)
print(f'V_U = {V_U:.2f}')

plt.scatter([V_U],[0],c='magenta', label = f'$V_U = ({V_U:.2f}\pm 0.2) V$')

#Resistencia Dinamica 
# Es la inversa de la pendiente 
R_D = 1/a
print(f'R_D = {R_D:.2f}')

#Resistencia estatica 



#Corriente inversa de saturacion 
x = x.copy()/max(x)
y = y.copy()/max(y)

reg_func = lambda x,a,b: a*(np.exp(b*x)-1)
coef,cov = curve_fit(reg_func, x,y)
a,b = coef
print(coef)

I_0 = a*max(I_D)
print(a)

print(f'I_0 = {I_0: .2e} ')

xx = np.linspace(0,1,50)
yy = reg_func(xx,a,b)
plt.plot(xx*max(V_D),yy*max(I_D),c="purple",label = f'$I_0 = {I_0: .2e}$')

#Constante de boltzman 

#Voltaje termico 

#Punto Q 