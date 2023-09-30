import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
#|%%--%%| <S7D56Q76gG|q366fMaDZF>

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

#|%%--%%| <q366fMaDZF|L4ZV5NsvOM>
name = '2_diodos_serie'
raw_data = pd.read_csv(f'{name}.csv')
raw_data

#|%%--%%| <L4ZV5NsvOM|pG1ifQWwyd>

I_D = raw_data['I_D']
V_D = raw_data['V_D']

#|%%--%%| <pG1ifQWwyd|PaOU9xssBN>

y = I_D.copy()#/max(I_D)
x = V_D.copy()#/max(V_D)

plt.scatter(x,y)
plt.xlabel(f'$V_D (V)$', color = "black")
plt.ylabel(f'$I_D (A)$', color = "black")
plt.title('Voltaje vs Corriente de carga', color = "black")
plt.grid()

#Voltaje umbral 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x[15:],y[15:])
a,b = coef
print(f'coef. lineal: {coef}')

xx = np.linspace(1.2,1.44,50)
yy = reg_func(xx,a,b)

plt.plot(xx,yy,c="green",label = f'$({a: .2f}\pm 0.02)*V_0 + ({b:.2f}\pm 0.02)$')

reg_func_inv = lambda y,a,b: (y-b)/a
V_U = reg_func_inv(0,a,b)
print(f'V_U = {V_U:.2f}')

plt.scatter([V_U],[0],c='magenta', label = f'$V_U = ({V_U:.2f}\pm 0.05) [V]$')

#Resistencia Dinamica 
# Es la inversa de la pendiente 
R_D = 1/a
print(f'R_D = {R_D:.2f}')

#Resistencia estatica 
R = 100 #ohm
R_e = R_D+R
print(f'R_e = {R_e:.2f}')


#Corriente inversa de saturacion 
x = x.copy()/max(x)
y = y.copy()/max(y)

reg_func = lambda x,a,b: a*(np.exp(b*x)-1)
coef,cov = curve_fit(reg_func, x,y)
a,b = coef
print(f'coef. exponencial: {coef}')

I_0 = a*max(I_D)

print(f'I_0 = {I_0: .2e} ')

xx = np.linspace(0,1,50)
yy = reg_func(xx,a,b)
plt.plot(xx*max(V_D),yy*max(I_D),c="purple",label = f'$({latex_float(a)}\pm 0.3)*[e^{{({b:.1f}\pm 0.7)}}-1]$')

#Constante de boltzman 
q = 1.6e-19 
eta = 1 
T = 294 
k_B = q/(eta*b*T)*max(V_D)
print(f'k_B = {k_B}')

#Punto Q 
V_S = 1.9
V_SR = V_S/R
plt.scatter([V_S,0],[0,V_SR],label = '$(V_S,V_S/R_S)$')

reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, [V_S,0],[0,V_SR])
a,b = coef
print(f'coef. exponencial: {coef}')

xx = np.linspace(0,1.9,50)
yy = reg_func(xx,a,b)

plt.plot(xx,yy)

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'
plt.savefig(f'{name}.jpg')
