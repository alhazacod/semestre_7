import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

raw_data = pd.read_csv('sin_capacitor.csv')
print(raw_data)

x = raw_data['f']
y = raw_data['Ganancia']

plt.plot(x,y,marker = 'o')
plt.xscale("log")
plt.axvline(x=4.8, color='black', linestyle='--')
plt.axvline(x=360000, color='black', linestyle='--')
plt.axhline(y=2.7, color='r', linestyle='--')
plt.text(100,2.5,'BW=360khz')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Ganancia')
plt.show()
