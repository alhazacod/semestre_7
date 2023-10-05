from sage.all import *
from sage.symbolic.integration.integral import definite_integral
from sage.calculus.calculus import symbolic_sum
from sympy import fourier_transform

x, p, w = var('x p w', domain = 'real')
assume(w>0)
assume(p>0)
N = 1  
hbar = var('hbar')
assume(hbar>0)
#psi_p_x(x) = N * exp(I * (p * x / hbar))
psi_p_x(x) = N*(cos(p*x/hbar) + I*sin(p*x/hbar))

trans1 = integral(N*(cos(p*x/hbar)*exp(-2*pi*I*x*w)), (x,-oo,oo))
print(f'transf1 {trans1}')
trans2 = integral(N*(I*sin(p*x/hbar)*exp(-2*pi*I*x*w)), (x,-oo,oo))
print(f'transf2 {trans2}')

transformada(w) = integral((psi_p_x(x)*exp(-2*pi*I*x*w)),(x,-oo,oo))
print(transformada)
