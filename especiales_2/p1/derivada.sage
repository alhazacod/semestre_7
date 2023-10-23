z = var('z', domain='complex')
f(z) = 2*z^2+3*z+1 
g(z) = z+I/z
h(z) = (z-1)^2
fg(z) = f(g(z))
gh(z) = g(h(z))
func(z) = fg(z)-gh(z)
deriv(z) = derivative(func(z),z)
print(deriv(z))
deriv(2-3*I)
