from sage.all import *

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

def calc_first_derivatives(surface ):
    first_derivative_ = surface.natural_frame()
    first_derivative = {'u': first_derivative_[1], 'v': first_derivative_[1]}
    return first_derivative
    

def calc_second_derivatives(surface ):
    first_derivative = calc_first_derivatives(surface)
    second_derivative = {'uu': derivative(first_derivative['u'],u),
                         'uv': derivative(first_derivative['u'],v),
                         'vv': derivative(first_derivative['v'],v),
                         'vu': derivative(first_derivative['v'],u),}
    return second_derivative

def dot_products(surface ):
    first_derivative = calc_first_derivatives(surface)
    second_derivative = calc_second_derivative(surface)
    normal = surface.normal_vector()

u,v,a,b = var('u,v,a,b',domain='real')

eq = [a*cos(u)*cos(v), a*sin(u)*cos(v), a*sin(v)]
surface = ParametrizedSurface3D(eq, [u,v])

print(f'{surface}\n')

print('First derivatives: ')
print_dict(calc_first_derivatives(surface))
print('\n')

print('Second derivatives:')
print_dict(calc_second_derivatives(surface))
print('\n')

normal = surface.normal_vector()
normal_normalized = normal.normalized()
print(f'Vector normal: {normal} ')
print(f'Vector normal normalizado: {normal_normalized}')
print('\n')

print('First fundamental form:')
print_dict(surface.first_fundamental_form_coefficients())
print('\n')

print('Second fundamental form:')
print_dict(surface.second_fundamental_form_coefficients())
print('\n')

for k in calc_second_derivatives(surface):
    print(f'Ñ dot {k}: {normal_normalized.dot_product(calc_second_derivatives(surface)[k]).full_simplify()}')
