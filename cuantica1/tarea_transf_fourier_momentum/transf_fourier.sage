from sage.all import *
from sage.symbolic.integration.integral import definite_integral
from sage.calculus.calculus import symbolic_sum
from sympy import fourier_transform

x, p, w = var('x p w')
N = 1  
hbar = var('hbar')
psi_p_x(x) = N * exp(I * (p * x / hbar))

transformada(w) = integral((psi_p_x(x)*exp(-2*pi*I*x*w)),(x,-oo,oo))
print(transformada)
