from sage.all import *

x, x_0, w = var('x x_0 w', domain = 'real')
assume(w>0)
hbar, N = var('hbar N', domain = 'real')
assume(hbar>0)

psi_x = N*exp(-x^2/2)

transformada = 1/sqrt(2*pi)*integral(psi_x*exp(-I*w*x),(x,-oo,oo))
print(latex(transformada))
