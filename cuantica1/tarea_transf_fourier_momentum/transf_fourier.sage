from sage.all import *

x, x_0, w = var('x x_0 w', domain = 'real')
assume(w>0)
hbar,xbar = var('hbar xbar', domain = 'real')
assume(hbar>0)

psi_x = (1/(x_0*sqrt(pi)))**(1/2)*exp(-1/2*(x/xbar)**2)

transformada = integral(psi_x*exp(-2*pi*I*x*w)),(x,-oo,oo))
