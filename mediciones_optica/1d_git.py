############## MODULES IMPORTATION ###############
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def anim_1D(x,y, pas_de_temps, pas_d_images, save = False, myxlim = (0, 4) , myylim = (-4,4)):

    fig = plt.figure()
    ax = plt.axes(xlim= myxlim , ylim= myylim)
    line, = ax.plot([], [])
    ax.set_title("t = 0 s", fontname = "serif", fontsize = 16)
    ax.set_xlabel("x [m]", fontname = "serif", fontsize = 14)
    ax.set_ylabel("$u$ [m]", fontname = "serif", fontsize = 14)
    plt.axvline(x = 0.4, color = 'b', label = 'axvline - full height')
    plt.axvline(x = 0.7, color = 'b', label = 'axvline - full height')
    plt.axhline(y=0.5, color='r', linestyle='-')
    def init():
        line.set_data([],[])
        return line,
    
    # animation function.  This is called sequentially
    def animate(i):
        line.set_data(x, y[:,pas_d_images*i])
        ax.set_title("$u(x)$ à t = {} s".format(np.round(i*pas_d_images*pas_de_temps, 4)), fontname = "serif", fontsize = 16)
        return line,
        
    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=y.shape[1]//pas_d_images, interval=10, blit=True)

    if save:
        #writer = animation.FFMpegWriter(fps = 24, bitrate = 10000, codec = "libx264", extra_args = ["-pix_fmt", "yuv420p"])
        writer = animation.PillowWriter(fps=15, bitrate=1800)
        anim.save('file.gif',writer=writer)

    return anim


#Def of the initial condition    
def I(x):
    """
    the wave form at t = 0
    """
    return np.exp(-(x)**2/0.01)



############## SET-UP THE PROBLEM ###############

#Def of velocity (spatial scalar field)
# def celer(x):
#     """
#     constant velocity
#     """
#     return 1

def celer(x):
    """
    wave's velocity at a position x
    """
    if x >= 0.4 and x <= 0.7: 
        return 0.5 
    else: 
        return 1

def material(x):
    if x >= 0.4 and x <= 0.7: 
        return 0.005
    else: 
        return 0
      
        
#Spatial mesh - i indices
L_x = 1.5 #Range of the domain according to x [m]
dx = 0.01 #Infinitesimal distance
N_x = int(L_x/dx) #Points number of the spatial mesh
X = np.linspace(0,L_x,N_x+1) #Spatial array



#Temporal mesh with CFL < 1 - j indices
L_t = 4 #Duration of simulation [s]
dt = 0.01*dx  #Infinitesimal time with CFL (Courant–Friedrichs–Lewy condition)
N_t = int(L_t/dt) #Points number of the temporal mesh
T = np.linspace(0,L_t,N_t+1) #Temporal array



#Velocity array for calculation (finite elements)
c = np.zeros(N_x+1, float)
for i in range(0,N_x+1):
    c[i] = celer(X[i])

m = np.zeros(N_x+1, float)
for i in range(0,N_x+1):
    m[i] = material(X[i])


############## CALCULATION CONSTANTS ###############
c_1 = c[0]
c_2 = c[N_x]

C2 = (dt/dx)**2

CFL_1 = c_1*(dt/dx)
CFL_2 = c_2*(dt/dx)


############## PROCESSING LOOP ###############

u_jm1 = np.zeros(N_x+1,float)   #Vector array u_i^{j-1}
u_j = np.zeros(N_x+1,float)     #Vector array u_i^j
u_jp1 = np.zeros(N_x+1,float)   #Vector array u_i^{j+1}

q = np.zeros(N_x+1,float)
q[0:N_x+1] = c[0:N_x+1]**2

U = np.zeros((N_x+1,N_t+1),float) #Global solution

#init cond - at t = 0
u_j[0:N_x+1] = I(X[0:N_x+1])
U[:,0] = u_j.copy()

 
#init cond - at t = 1
#without boundary cond
u_jp1[1:N_x] = (u_j[1:N_x] + 0.5 * C2 * (0.5 * (q[1:N_x] + q[2:N_x+1]) * (u_j[2:N_x+1] - u_j[1:N_x]) - 0.5 * (q[0:N_x-1] + q[1:N_x]) * (u_j[1:N_x] - u_j[0:N_x-1])) )- m[1:N_x]* dt * u_j[1:N_x]


    
#Nuemann bound cond
#i = 0
u_jp1[0] = u_j[0] + 0.5*C2*( 0.5*(q[0] + q[0+1])*(u_j[0+1] - u_j[0]) - 0.5*(q[0] + q[0+1])*(u_j[0] - u_j[0+1]))

#Mur bound cond
#i = N_x
u_jp1[N_x] = u_j[N_x-1] + (CFL_2 -1)/(CFL_2 + 1)*(u_jp1[N_x-1] - u_j[N_x])


u_jm1 = u_j.copy()  #go to the next step
u_j = u_jp1.copy()  #go to the next step
U[:,1] = u_j.copy()


#Process loop (on time mesh)
for j in range(1, N_t):
    #material_vector = material(N_x) 
    #calculation at step j+1
    #without boundary cond
    u_jp1[1:N_x] = (-u_jm1[1:N_x] + 2*u_j[1:N_x] + C2*( 0.5*(q[1:N_x] + q[2:N_x+1])*(u_j[2:N_x+1] - u_j[1:N_x]) - 0.5*(q[0:N_x-1] + q[1:N_x])*(u_j[1:N_x] - u_j[0:N_x-1])) )- m[1:N_x]* dt * u_j[1:N_x]
       
    
    #Nuemann bound cond
    #i = 0
    u_jp1[0] = -u_jm1[0] + 2*u_j[0] + C2*( 0.5*(q[0] + q[0+1])*(u_j[0+1] - u_j[0]) - 0.5*(q[0] + q[0+1])*(u_j[0] - u_j[0+1]))       
        

    #Mur bound cond
    #i = N_x
    u_jp1[N_x] = u_j[N_x-1] + (CFL_2 -1)/(CFL_2 + 1)*(u_jp1[N_x-1] - u_j[N_x])

   
    
    u_jm1[:] = u_j.copy()   #go to the next step
    u_j[:] = u_jp1.copy()   #go to the next step
    U[:,j] = u_j.copy()




############## PLOT ###############

anim1 = anim_1D(X,U, dt, 10, save = True , myxlim = (0, 1.5) , myylim = (-0.5,1.5))
plt.show()
