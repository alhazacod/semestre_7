import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
#imports para la regresion 
from scipy.optimize import curve_fit
#para hallar el punto de interseccion 
from scipy.optimize import fsolve
#Para hallar el maximo de una funcion 
from scipy.optimize import minimize_scalar
#|%%--%%| <cypJM4gzYu|QLMreBgM8g>
raw_data = pd.read_csv("datos_thevenin_norton.csv")

print(raw_data)

#|%%--%%| <QLMreBgM8g|QJmMB5flHd>
# Voltaje vs corriente y punto de corte con V_L = 1kohm*I_L
x = raw_data['V_L (V)']
y = raw_data['I_L (mA)']

#|%%--%%| <QJmMB5flHd|DDbFDksNb3>
# Graficamos los datos medidos
plt.scatter(x,y,label = "Datos obtenidos")
plt.xlabel(f'$V_L (V)$', color = "black")
plt.ylabel(f'$I_L (mA)$', color = "black")
plt.title('Voltaje vs Corriente de carga', color = "black")
plt.grid()

#Realizamos la regresion 
reg_func = lambda x,a,b: a*x+b
coef,cov = curve_fit(lambda x,a,b: a*x+b, x,y)
a,b = coef

xx = x
yy = reg_func(x,a,b)

residuals = y - yy
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)

# Graficamos la regresion lineal 
plt.plot(xx,yy,c="green", label = f"$I_L = ({a:.2f}±{0.01:.2f})*V_L + ({b:.2f}±{0.01:.2f}), R^2 = 0.98$")

#Graficamos Caracteristica de la resistencia de 1kohm
x_1ko = x[4:-11]
y_1ko = 1*x_1ko
plt.plot(x_1ko,y_1ko,c="black", label = "Recta caracteristica de $1k\Omega$")

# Encontramos el punto de corte 
def equations(p):
    x, y = p
    eq1 = a * x + b - y
    eq2 = 1 * x - y
    return [eq1, eq2]
intersection_point = fsolve(equations, [1.5,1.5])
plt.scatter([intersection_point[0]],[intersection_point[1]], c = "magenta", label = f"Punto de corte ({intersection_point[0]:.2f},{intersection_point[1]:.2f})", marker=",",s = 70)

plt.legend()
plt.rcParams['axes.facecolor'] = 'white'

plt.savefig("Voltaje_vs_corriente_de_carga.jpg")

#|%%--%%| <DDbFDksNb3|IFcMRBAsMl>
r"""°°°
Potencia vs resistencia de carga
°°°"""
#|%%--%%| <IFcMRBAsMl|rnidtV93L7>

# Potencia 
x = raw_data['R_L'] # Resistencia de carga 
y = raw_data['I_L (mA)']**2*raw_data['R_L'] # potencia 

#|%%--%%| <rnidtV93L7|5Kc7hdB8yv>

# Grafica de la potencia vs resistencia de carga 

plt.scatter(x,y,label = "Potencia vs Resistencia de Carga")
plt.xlabel(r'$R_L (k\Omega)$', color = "black")
plt.ylabel(r'$P_{R_L} (mW)$', color = "black")
plt.title('Potencia vs Resistencia de carga', color = "black")
plt.grid()

#Realizamos la regresion 
reg_func = lambda x,a,b,c: x/(a*x**2+b*x+c)
coef,cov = curve_fit(reg_func, x,y)
a,b,c = coef

xx = np.linspace(min(x),max(x),100)
yy = reg_func(xx,a,b,c)

plt.plot(xx,yy,c="green", label='Linea de tendencia')

#Encontramos el maximo de la regresion 
maximo = minimize_scalar(lambda x: -reg_func(x,a,b,c), method='bounded', bounds=(0, 10))

plt.scatter([maximo.x],[-maximo.fun],c="magenta", marker = '^', s=120, label = f'Punto Maximo ({maximo.x:.2f},{-maximo.fun:.2f})')

plt.legend()

plt.savefig('potencia_vs_corriente_de_carga.jpg')
