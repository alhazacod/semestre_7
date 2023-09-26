from sage.all import *
import numpy as np

r,phi,theta = var('r,phi,theta',domain = 'real')

eq = [r*cos(phi)*sin(theta),r*sin(theta)*sin(phi), r*cos(theta)]

# Jacobiano
print('Jacobiano: ')
print(jacobian(eq, (r,theta,phi)))
print(jacobian(eq, (r,theta,phi)).determinant().simplify_full())
print('\n')
