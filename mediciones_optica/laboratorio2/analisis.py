import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#imports para la regresion 
from scipy.optimize import curve_fit
#|%%--%%| <ZfUEyeursi|xHZu65bEfV>

raw_data = pd.read_csv('data_focos.csv')
raw_data.columns = ['D_o','D_i','Dis_puntos']
print(raw_data)

#|%%--%%| <xHZu65bEfV|2DuZqxdAZk>

x = raw_data['D_o']+raw_data['D_i']
y = raw_data['D_o']*raw_data['D_i']

plt.scatter(x,y,label = 'Datos obtenidos')
plt.xlabel(f'$S_0+S_i [cm]$', color = "black")
plt.ylabel(f'$S_oS_i [cm^2]$', color = "black")
plt.title('Suma de las distancias vs Producto de las distancias', color = "black")
plt.grid()


#Realizamos la regresion 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x,y)
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b = coef

residuals = y- reg_func(x, a,b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)


xx = np.linspace(50,110,50)
yy = reg_func(xx,a,b)

# Graficamos la regresion  
plt.plot(xx,yy,c="green",label=f'$S_0S_i = (S_0+S_i)*({a:.2f}\pm {cov[0,0]:.2f})+({b:.2f}\pm {cov[0,0]:.2f})$\n $R^2 = {r_squared:.3f}$')

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'
plt.savefig('Suma_producto.jpg')

#|%%--%%| <2DuZqxdAZk|BjBWazCwG7>

x = 1/raw_data['D_o']
y = 1/raw_data['D_i']

plt.scatter(x,y)

plt.scatter(x,y,label = 'Datos obtenidos')
plt.xlabel(f'$1/S_o [1/cm]$', color = "black")
plt.ylabel(f'$1/S_i [1/cm]$', color = "black")
plt.title('Inverso de las distancias', color = "black")
plt.grid()


#Realizamos la regresion 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x,y)
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b = coef

residuals = y- reg_func(x, a,b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)


xx = x
yy = reg_func(xx,a,b)

# Graficamos la regresion  
plt.plot(xx,yy,c="green",label=f'$1/S_i = 1/S_0*({a:.2f}\pm 0.05)+({b:.2f}\pm 0.01)$\n $R^2 = {r_squared:.3f}$')

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'
plt.savefig('inv_dis.jpg')

#|%%--%%| <BjBWazCwG7|gSHC7O7pzU>

m = raw_data['Dis_puntos']/0.2
y = 1/m
x = raw_data['D_o']

plt.scatter(x,y,label = 'Datos obtenidos')
plt.xlabel(f'$S_o [cm]$', color = "black")
plt.ylabel(f'$1/m$', color = "black")
plt.title('Inverso de la magnificacion', color = "black")
plt.grid()


#Realizamos la regresion 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(reg_func, x,y)
# La regresion da unos valores muy cercanos pero cambié manualmente el c para que diera mejor el ajuste
a,b = coef

residuals = y- reg_func(x, a,b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)


xx = x
yy = reg_func(xx,a,b)

# Graficamos la regresion  
plt.plot(xx,yy,c="green",label=f'$1/m = S_0*({a:.2f}\pm 0.01)+({b:.2f}\pm 0.01)$\n $R^2 = {r_squared:.3f}$')

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'
plt.savefig('inv_magnificacion.jpg')

