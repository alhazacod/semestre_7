import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

raw_data = pd.read_csv('IDvsVDS_negativo.csv')
print(raw_data)

x = raw_data['V_DS']
y = raw_data['I_D']

plt.plot(x,y, label = 'Curva transferencia FET', marker = '.')
plt.xlabel(f'$V_{{DS}}(V)$')
plt.ylabel(f'$I_D(A)$')
plt.legend()
plt.grid()
plt.show()
