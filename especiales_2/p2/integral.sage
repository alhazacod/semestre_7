x,y = var('x,y', domain = 'real')
# Define the function
z = x+I*y
f = (z^2+4)/sin(pi*z)

# Define the contour
C = circle((0,0), 1)

# Compute the integral
integral(f, C)
