from sage.all import *

y, p, N, xbar, x = var('y p N xbar x', domain = 'real')
hbar = var('hbar', domain = 'real', latex_name = '\\hbar')
assume(hbar>0)
assume(xbar>0)

psi_x = N*hermite(2,y)*exp(-y^2/2)
#psi_x = exp(-1/2*x^2/xbar^2)
print(f'psi_x: {psi_x}')

transformada = 1/sqrt(2*pi*hbar)*integral(psi_x*exp(-I*p*y/hbar),(y,-oo,oo))
#transformada = integral(psi_x*cos(p*x/hbar),(x,-oo,oo))
print(latex(transformada.simplify_full()))

#for i in range(10):
#    print(hermite(i,x))
