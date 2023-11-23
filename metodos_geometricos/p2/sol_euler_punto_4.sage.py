

# This file was *autogenerated* from the file sol_euler_punto_4.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2)
from sage.manifolds.operators import *


# Definir las variables y la función de lagrangiano
var('t a')
M = Manifold(_sage_const_3 , 'M', structure='Euclidean')
C = M.cartesian_coordinates()
r = M.point((C[_sage_const_0 ], C[_sage_const_1 ], sqrt(C[_sage_const_0 ]**_sage_const_2  + C[_sage_const_1 ]**_sage_const_2 )))
v = M.tangent_space(r)
L = _sage_const_1 /_sage_const_2  * v.norm()**_sage_const_2  - a * cross_product(r, v).norm() / r.norm()

# Definir las ecuaciones de Euler-Lagrange
ELeqs = [diff(L.diff(v[i]), t) - L.diff(C[i]) for i in range(_sage_const_3 )]

# Resolver las ecuaciones de Euler-Lagrange
sol = desolve_system(ELeqs, [C[_sage_const_0 ](t), C[_sage_const_1 ](t), C[_sage_const_2 ](t)], ics=[_sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 ], ivar=t)

# Verificar la condición del cono circular
cone_condition = sol[_sage_const_2 ].subs(sqrt(C[_sage_const_0 ]**_sage_const_2  + C[_sage_const_1 ]**_sage_const_2 ), C[_sage_const_2 ])

# Mostrar las soluciones y la condición del cono circular
print("Soluciones:")
print(sol)
print("\nCondición del cono circular:")
print(cone_condition)


