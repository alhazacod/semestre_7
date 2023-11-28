import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

raw_data = pd.read_csv('IDvsVDS.csv')
print(raw_data)

x = raw_data['V_DS']
y = raw_data['I_D']

plt.scatter(x,y)
plt.xlabel(f'$V_{{DS}}(V)$')
x_pinch_off = x[4]
y_pinch_off = y[4]
plt.scatter(x_pinch_off,y_pinch_off, label = 'Pinch Off')
plt.ylabel(f'$I_D(A)$')
plt.legend()
plt.grid()
plt.show()
