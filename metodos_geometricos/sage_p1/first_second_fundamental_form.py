from sage.all import *

u,v,a,b = var('u,v,a,b',domain='real')

eq = [a*cos(u)*cos(v), a*sin(u)*cos(v), a*sin(v)]

surface = ParametrizedSurface3D(eq, [u,v])

first_derivative = surface.natural_frame()
print(first_derivative)

second_derivative_u = derivative(first_derivative[1],u)
print(second_derivative_u)
