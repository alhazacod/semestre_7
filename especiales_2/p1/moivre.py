
from sage.all import *

#|%%--%%| <XZRIDzFNuC|SR3pzQSHS6>
n = 10
#|%%--%%| <SR3pzQSHS6|oTkdbgoUSA>

for theta in [0,pi/3,pi/4,pi/2,3*pi/2]:
    print(f'para {theta} = {N(sin(n*theta))}')
    r = N(sum([factorial(n)/(factorial(2*p)*factorial(n-2*p))*(cos(theta))**(n-2*p)*(sin(theta))**(2*p) for p in range(0,ceil(n/2)) ]))
    print(f'r: {r}')
    print('\n')

#|%%--%%| <oTkdbgoUSA|1il30kYTWg>

for theta in [0,pi/3,pi/4,pi/2,3*pi/2]:
    print(f'para {theta} = {N(sin(n*theta))}')
    r = N(sum([factorial(n)*(-1)**p/( factorial(2*p+1) * factorial(n-2*p-1) )*(cos(theta))**(n-2*p-1)*(sin(theta))**(2*p+1) for p in range(0,ceil((n-1)/2)) ]))
    print(f'r: {r}')
    print('\n')

#|%%--%%| <1il30kYTWg|5Ay4sowBIn>


for theta in [0,pi/3,pi/4,pi/2,3*pi/2]:
    print(f'para {theta} = {N(cos(n*theta))}')
    r = N(sum([factorial(n)*(-1)**p/( factorial(2*p+1)*factorial(n-2*p-1) )*(cos(theta))**(n-2*p-1)*(sin(theta))**(2*p+1) for p in range(0,ceil(n/2)) ]))
    print(f'r: {r}')
    print('\n')

#|%%--%%| <5Ay4sowBIn|Mio4mITKUf>


for theta in [0,pi/3,pi/4,pi/2,3*pi/2]:
    print(f'para {theta} = {N(cos(n*theta))}')
    r = N(sum([factorial(n)*(-1)**p/( factorial(2*p)*factorial(n-2*p) ) * (cos(theta))**(n-2*p)*(sin(theta))**(2*p) for p in range(0,ceil((n-1)/2)) ]))
    print(f'r: {r}')
    print('\n')

