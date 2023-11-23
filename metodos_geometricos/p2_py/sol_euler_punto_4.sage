from sage.manifolds.operators import *


# Definir las variables y la función de lagrangiano
var('t a')
M = Manifold(3, 'M', structure='Euclidean')
C = M.cartesian_coordinates()
r = M.point((C[0], C[1], sqrt(C[0]^2 + C[1]^2)))
v = M.tangent_space(r)
L = 1/2 * v.norm()^2 - a * cross_product(r, v).norm() / r.norm()

# Definir las ecuaciones de Euler-Lagrange
ELeqs = [diff(L.diff(v[i]), t) - L.diff(C[i]) for i in range(3)]

# Resolver las ecuaciones de Euler-Lagrange
sol = desolve_system(ELeqs, [C[0](t), C[1](t), C[2](t)], ics=[0, 0, 0, 1, 0, 1], ivar=t)

# Verificar la condición del cono circular
cone_condition = sol[2].subs(sqrt(C[0]^2 + C[1]^2), C[2])

# Mostrar las soluciones y la condición del cono circular
print("Soluciones:")
print(sol)
print("\nCondición del cono circular:")
print(cone_condition)

