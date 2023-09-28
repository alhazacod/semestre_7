t,x = var('t x')

# Creamos una variedad de dimension 2 con structura lorentziana
M = Manifold(2, 'M', structure='Lorentzian')
print(M)

X.<x,y> = M.chart('t x')
X_f = X.frame()
g = M.metric()
g[0,0] = -1
g[1,1] = 1 
print(g[:])

# Transformacion
xplus,xminus = var('xplus xminus')
XPM.<xplus,xminus> = M.chart('xplus xminus')
print(XPM)

transformation = XPM.transition_map(X, [1/2 * (xplus + xminus), 1/2 *(xplus-xminus)])
print(transformation.inverse().display())
print(g.display(XPM.frame()))
print(g[XPM.frame(),:])

##############################################
psi,zeta = var('psi zeta')
PZ.<psi,zeta> = M.chart('psi zeta')
transformation_pz_pm = PZ.transition_map(XPM, [tan(1/2*(psi+zeta)), tan(1/2*(psi-zeta))])
transformation_pz_pm.set_inverse(atan(xplus) + atan(xminus), atan(xplus) - atan(xminus))
print(transformation_pz_pm.inverse().display())
print(latex( -g[PZ.frame(),0,0].expr().substitute(arctan(xp)==1/2*(psi+zeta),arctan(xm)==1/2*(psi-zeta)).factor()))
