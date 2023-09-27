from sage.all import * 

t = var('t', domain = 'real')

r = vector((1/2 - t**2, t*sqrt(1-t**2), t))

rd = r.diff(t)
print(f'rd = {latex(rd)}')
rdd = rd.diff(t)
print(f'rdd = {latex(rdd)}')
rddd = rdd.diff(t)
print(f'rddd = {latex(rddd)}')

print('\n')

rd_cross_rdd = rd.cross_product(rdd)
norm_rd_cross_rdd = rd_cross_rdd.norm()

norm_rd = rd.norm()

kappa = norm_rd_cross_rdd/norm_rd**3
print(f'kappa = {latex(kappa.full_simplify())}')

chi = - rd*(rdd.cross_product(rddd))/(rd.cross_product(rdd)).norm()
print(f'chi = {latex(chi.full_simplify())}')

print(f'\n {latex(rd*(rdd.cross_product(rddd)))}')
