# Definir las variables y la función
var('t a')
r, v = function('r')(t), function('v')(t)

# Definir el sistema de ecuaciones diferenciales
sistema_ecuaciones = [
    diff(r, t) == v,
    diff(v, t) == a * abs(v) / abs(r)^2
]

# Condiciones iniciales (cámbialas según tus necesidades)
condiciones_iniciales = [r(0) == r0, v(0) == v0]

# Resolver el sistema de ecuaciones diferenciales
solucion = desolve_system(
    sistema_ecuaciones,
    [r, v],
    ics=condiciones_iniciales,
    algorithm='rk4'
)

# Mostrar la solución
show(solucion)

