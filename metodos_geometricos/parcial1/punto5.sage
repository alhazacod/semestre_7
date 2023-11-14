t,x = var('t x')

# Creamos una variedad de dimension 2
M = Manifold(2, 'M', structure='Lorentzian')
print(M)

#Espacio "original" en t,x
X.<t,x> = M.chart('t x')
X_f = X.frame()
print(f'X frame: {X_f}')
g = M.metric()
g[0,0] = -1
g[1,1] = 1 
print(g[:])

# Transformacion hacia psi,zeta
psi,zeta = var('psi zeta')
PZ.<psi,zeta> = M.chart('psi zeta')
print(f'PZ: {PZ}')

transformation = PZ.transition_map(X, [1/2*tan(1/2*(psi+zeta))- 1/2*tan(1/2*(psi-zeta)), 1/2*tan(1/2*(psi+zeta))+ 1/2*tan(1/2*(psi-zeta))])
transformation.set_inverse(atan(t+x)+atan(t-x),atan(t+x)-atan(t-x))
print(f'frame: {PZ.frame()}')
print(latex(g.display(PZ)))
print(f'g[0,0]: {latex(g[PZ.frame(),0,0])}')
print(f'g[1,1]: {latex(g[PZ.frame(),1,1])}')


#####################################                            Anotaciones:                            #####################################
#
# Se logró calcular la metrica pero la expresion es extremadamente larga y no se logró identificar el facto omega.
#
# A continuacion dejo el resultado que se obtuvo para g en formato latex: 
#
#
# g = \left( \frac{\cos\left(\frac{1}{2} \, \zeta\right)^{4} - 2 \, \cos\left(\frac{1}{2} \, \zeta\right)^{2} \sin\left(\frac{1}{2} \, \psi\right)^{2} + \sin\left(\frac{1}{2} \, \psi\right)^{4}}{4 \, {\left(\cos\left(\frac{1}{2} \, \psi\right)^{8} \cos\left(\frac{1}{2} \, \zeta\right)^{8} - 4 \, \cos\left(\frac{1}{2} \, \psi\right)^{6} \cos\left(\frac{1}{2} \, \zeta\right)^{6} \sin\left(\frac{1}{2} \, \psi\right)^{2} \sin\left(\frac{1}{2} \, \zeta\right)^{2} + 6 \, \cos\left(\frac{1}{2} \, \psi\right)^{4} \cos\left(\frac{1}{2} \, \zeta\right)^{4} \sin\left(\frac{1}{2} \, \psi\right)^{4} \sin\left(\frac{1}{2} \, \zeta\right)^{4} - 4 \, \cos\left(\frac{1}{2} \, \psi\right)^{2} \cos\left(\frac{1}{2} \, \zeta\right)^{2} \sin\left(\frac{1}{2} \, \psi\right)^{6} \sin\left(\frac{1}{2} \, \zeta\right)^{6} + \sin\left(\frac{1}{2} \, \psi\right)^{8} \sin\left(\frac{1}{2} \, \zeta\right)^{8}\right)}} \right) \mathrm{d} \psi\otimes \mathrm{d} \psi + \left( -\frac{\cos\left(\frac{1}{2} \, \zeta\right)^{4} - 2 \, \cos\left(\frac{1}{2} \, \zeta\right)^{2} \sin\left(\frac{1}{2} \, \psi\right)^{2} + \sin\left(\frac{1}{2} \, \psi\right)^{4}}{4 \, {\left(\cos\left(\frac{1}{2} \, \psi\right)^{8} \cos\left(\frac{1}{2} \, \zeta\right)^{8} - 4 \, \cos\left(\frac{1}{2} \, \psi\right)^{6} \cos\left(\frac{1}{2} \, \zeta\right)^{6} \sin\left(\frac{1}{2} \, \psi\right)^{2} \sin\left(\frac{1}{2} \, \zeta\right)^{2} + 6 \, \cos\left(\frac{1}{2} \, \psi\right)^{4} \cos\left(\frac{1}{2} \, \zeta\right)^{4} \sin\left(\frac{1}{2} \, \psi\right)^{4} \sin\left(\frac{1}{2} \, \zeta\right)^{4} - 4 \, \cos\left(\frac{1}{2} \, \psi\right)^{2} \cos\left(\frac{1}{2} \, \zeta\right)^{2} \sin\left(\frac{1}{2} \, \psi\right)^{6} \sin\left(\frac{1}{2} \, \zeta\right)^{6} + \sin\left(\frac{1}{2} \, \psi\right)^{8} \sin\left(\frac{1}{2} \, \zeta\right)^{8}\right)}} \right) \mathrm{d} \zeta\otimes \mathrm{d} \zeta
#
#
#g[0,0]: \frac{1}{4 \, {\left(4 \, {\left(4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{4} - 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{2} + 1\right)} \cos\left(\frac{1}{2} \, \arctan\left(t + x\right)\right)^{4} + 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{4} - 4 \, {\left(4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{4} - 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{2} + 1\right)} \cos\left(\frac{1}{2} \, \arctan\left(t + x\right)\right)^{2} - 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{2} + 1\right)}}
#
#
#g[1,1]: -\frac{1}{4 \, {\left(4 \, {\left(4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{4} - 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{2} + 1\right)} \cos\left(\frac{1}{2} \, \arctan\left(t + x\right)\right)^{4} + 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{4} - 4 \, {\left(4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{4} - 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{2} + 1\right)} \cos\left(\frac{1}{2} \, \arctan\left(t + x\right)\right)^{2} - 4 \, \cos\left(\frac{1}{2} \, \arctan\left(-t + x\right)\right)^{2} + 1\right)}}
