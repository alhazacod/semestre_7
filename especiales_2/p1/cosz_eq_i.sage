for k in range(0,5):
    print(f'Para k = {k}')
    a = 2/( sinh( (2*k+1)*pi )*cos(   (-1)^(k+1)*log(1+sqrt(2)) ) + I*cosh( (2*k+1)*pi )*sin( (-1)^(k + 1)*log(sqrt(2) + 1) ) )
    b = 2/( sinh( (2*k+1)*pi )*cos( 2*(-1)^(k+1)*log(1+sqrt(2)) ) + I*cosh( (2*k+1)*pi )*sin( 2*(-1)^(k+1)*log(1+sqrt(2)) ) )
    c = 2/( sinh( (2*k+1)*pi )*sin( 2*(-1)^(k+1)*log(1+sqrt(2)) ) + I*cosh( (2*k+1)*pi )*cos( 2*(-1)^(k+1)*log(1+sqrt(2)) ) )
    d = 2/( sinh( (2*k+1)*pi )*sin(   (-1)^(k+1)*log(1+sqrt(2)) ) + I*cosh( (2*k+1)*pi )*cos((-1)^(k+1)*log(1+sqrt(2))))

    print(f'a = {N(a)}')
    print(f'b = {N(b)}')
    print(f'c = {N(c)}')
    print(f'd = {N(d)}')

    sol(arg) = 1/2*cos(1/2*arcsinh(2/arg)) #2*pi*k + arccos(-i)

    print(N(sol(a)))
    print(N(sol(b)))
    print(N(sol(c)))
    print(N(sol(d)))

    #print(f'coth-tanh = {N(coth(sol)-tanh(sol))} \n')

    
print(f'{N(coth(arccos(-i))-tanh(arccos(-i)))}')
