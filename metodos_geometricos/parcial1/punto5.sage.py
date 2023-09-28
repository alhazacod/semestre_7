

# This file was *autogenerated* from the file punto5.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1)
t,x = var('t x')

# Creamos una variedad de dimension 2 con structura lorentziana
M = Manifold(_sage_const_2 , 'M', structure='Lorentzian')
print(M)

X = M.chart('t x', names=('x', 'y',)); (x, y,) = X._first_ngens(2)
X_f = X.frame()
g = M.metric()
g[_sage_const_0 ,_sage_const_0 ] = -_sage_const_1 
g[_sage_const_1 ,_sage_const_1 ] = _sage_const_1  
print(g[:])

# Transformacion
xplus,xminus = var('xplus xminus')
XPM = M.chart('xplus xminus', names=('xplus', 'xminus',)); (xplus, xminus,) = XPM._first_ngens(2)
print(XPM)

transformation = XPM.transition_map(X, [_sage_const_1 /_sage_const_2  * (xplus + xminus), _sage_const_1 /_sage_const_2  *(xplus-xminus)])
print(transformation.inverse().display())
print(g.display(XPM.frame()))
print(g[XPM.frame(),:])

# Coordenadas conformes
psi,zeta = var('psi zeta')
U = M.chart('psi zeta', names=('psi', 'zeta',)); (psi, zeta,) = U._first_ngens(2)

##############################################
psi,zeta = var('psi zeta')
PZ = M.chart('psi zeta', names=('psi', 'zeta',)); (psi, zeta,) = PZ._first_ngens(2)
transformation_pz_pm = PZ.transition_map(XPM, [tan(_sage_const_1 /_sage_const_2 *(psi+zeta)), tan(_sage_const_1 /_sage_const_2 *(psi-zeta))])
transformation_pz_pm.set_inverse(atan(xplus) + atan(xminus), atan(xplus) - atan(xminus))
print(transformation_pz_pm.inverse().display())
print(latex( -g[U.frame(),_sage_const_0 ,_sage_const_0 ].expr().substitute(arctan(xp)==_sage_const_1 /_sage_const_2 *(psi+zeta),arctan(xm)==_sage_const_1 /_sage_const_2 *(psi-zeta)).factor()))

