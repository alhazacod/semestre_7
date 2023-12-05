############## MODULES IMPORTATION ###############
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import meshgrid

def anim_2D(X, Y, L, pas_de_temps, pas_d_images, save = False, myzlim = (-0.15, 0.15)):
    
    fig = plt.figure(figsize = (8, 8), facecolor = "white")
    ax = fig.add_subplot(111, projection='3d')
    SX,SY = np.meshgrid(X,Y)
    surf = ax.plot_surface(SX, SY, L[:,:,0],cmap = plt.cm.RdBu_r)
    ax.set_zlim(myzlim[0], myzlim[1])
    ax.set_title("t = 0 s", fontname = "serif", fontsize = 16)

    elev_angle = 0; azim_angle = -93 #side
    #elev_angle = 90; azim_angle = -93 #top

    ax.view_init(elev=elev_angle, azim=azim_angle)
    
    # animation function
    def update_surf(num):
        ax.clear()
        surf = ax.plot_surface(SX, SY, L[:,:,pas_d_images*num],cmap = plt.cm.viridis)

        #Plot the material indication
        x = np.array([[2, 2], [2, 2]])
        y = np.array([[5, 0], [5, 0]])
        z = np.array([[0.15, 0.15], [-0.15, -0.15]])
        ax.plot_surface(x, y, z, color="gray", alpha=0.5)

        x = np.array([[3, 3], [3, 3]])
        y = np.array([[5, 0], [5, 0]])
        z = np.array([[0.15, 0.15], [-0.15, -0.15]])
        ax.plot_surface(x, y, z, color="red", alpha=0.5)
        
        
        ax.set_xlabel("x", fontname = "serif", fontsize = 14)
        ax.set_ylabel("y", fontname = "serif", fontsize = 14)
        ax.set_zlabel("$u$", fontname = "serif", fontsize = 16)
        ax.set_title("$u(x,y)$ en t = {:.1f} s".format(np.round(pas_d_images*num*pas_de_temps, 4)), fontname = "serif", fontsize = 16)
        ax.set_zlim(myzlim[0], myzlim[1])
        ax.set_ylim(0,5)
        ax.set_xlim(0,5)
        ax.view_init(elev=elev_angle, azim=azim_angle)
        plt.tight_layout()
        return surf,
        
    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, update_surf, frames = L.shape[2]//pas_d_images, interval = 50, blit = False)
    
    # Save the result
    if save:
        writer = animation.FFMpegWriter(fps = 24, bitrate = 10000, codec = "libx264", extra_args = ["-pix_fmt", "yuv420p"])
        #writer = animation.PillowWriter(fps=15, bitrate=1800)
        anim.save('file.mp4',writer=writer)
    
    return anim


#Def of the initial condition   
def I(x,y):
    """
    wave form at t = 0
    """
    return 0.2*np.exp(-((x-2.5)**2/0.2 + (y-0)**2/0.2))

def V(x,y):
    """
    initial vertical speed of the wave
    """
    return 0
    
    
    
############## SET-UP THE PROBLEM ###############

#Def of velocity (spatial scalar field)
def celer(x,y):
    if y >= 2 and y <= 3: 
        return 1
    else: 
        return 2
    
#Constant to aply the material absorption
def material(x,y):
    if y >= 2 and y <= 3: 
        return 0.002 
    else: 
        return 0


#Spatial mesh - i indices
L_x = 5 #Range of the domain according to x [m]
dx = 0.025 #Infinitesimal distance in the x direction
N_x = int(L_x/dx) #Points number of the spatial mesh in the x direction
X = np.linspace(0,L_x,N_x+1) #Spatial array in the x direction

#Spatial mesh - j indices
L_y = 5 #Range of the domain according to y [m]
dy = 0.025 #Infinitesimal distance in the x direction
N_y = int(L_y/dy) #Points number of the spatial mesh in the y direction
Y = np.linspace(0,L_y,N_y+1) #Spatial array in the y direction

#Temporal mesh with CFL < 1 - n indices
L_t = 5 #Duration of simulation [s]
dt = dt = 0.1*min(dx, dy)   #Infinitesimal time with CFL (Courant–Friedrichs–Lewy condition)
N_t = int(L_t/dt) #Points number of the temporal mesh
T = np.linspace(0,L_t,N_t+1) #Temporal array

#Velocity array for calculation (finite elements)
c = np.zeros((N_x+1,N_y+1), float)
for i in range(0,N_x+1):
    for j in range(0,N_y+1):
        c[i,j] = celer(X[i],Y[j])

m = np.zeros((N_x+1,N_y+1), float)
for i in range(0,N_x+1):
    for j in range(0,N_y+1):
        m[i,j] = material(X[i],Y[j])



############## CONSTANTS FOR FINITE ELEMENTS ###############
Cx2 = (dt/dx)**2
Cy2 = (dt/dy)**2 
CFL_1 = dt/dy*c[:,0]
CFL_2 = dt/dy*c[:,N_y]
CFL_3 = dt/dx*c[0,:]
CFL_4 =dt/dx*c[N_x,:]



############## PROCESSING LOOP ###############

U = np.zeros((N_x+1,N_x+1,N_t+1),float) 

u_nm1 = np.zeros((N_x+1,N_y+1),float)   #Vector array u_{i,j}^{n-1}
u_n = np.zeros((N_x+1,N_y+1),float)     #Vector array u_{i,j}^{n}
u_np1 = np.zeros((N_x+1,N_y+1),float)  #Vector array u_{i,j}^{n+1}
V_init = np.zeros((N_x+1,N_y+1),float)
q = np.zeros((N_x+1, N_y+1), float)

#init cond - at t = 0
for i in range(0, N_x+1):
    for j in range(0, N_y+1):
        q[i,j] = c[i,j]**2

for i in range(0, N_x+1):
    for j in range(0, N_y+1):
        u_n[i,j] = I(X[i],Y[j])
        
for i in range(0, N_x+1):
    for j in range(0, N_y+1):
        V_init[i,j] = V(X[i],Y[j])

U[:,:,0] = u_n.copy()



#init cond - at t = 1
#without boundary cond
u_np1[1:N_x,1:N_y] = 2*u_n[1:N_x,1:N_y] - (u_n[1:N_x,1:N_y] - 2*dt*V_init[1:N_x,1:N_y]) + Cx2*(  0.5*(q[1:N_x,1:N_y] + q[2:N_x+1,1:N_y ])*(u_n[2:N_x+1,1:N_y] - u_n[1:N_x,1:N_y])  - 0.5*(q[0:N_x -1,1:N_y] + q[1:N_x,1:N_y ])*(u_n[1:N_x,1:N_y] - u_n[0:N_x -1,1:N_y]) ) + Cy2*(  0.5*(q[1:N_x,1:N_y] + q[1:N_x ,2:N_y+1])*(u_n[1:N_x,2:N_y+1] - u_n[1:N_x,1:N_y])  - 0.5*(q[1:N_x,0:N_y -1] + q[1:N_x ,1:N_y])*(u_n[1:N_x,1:N_y] - u_n[1:N_x,0:N_y -1]) )- m[1:N_x,1:N_y]* dt * u_n[1:N_x,1:N_y]


#boundary conditions

i,j = 0,0
u_np1[i,j] = 2*u_n[i,j] - (u_n[i,j] - 2*dt*V_init[i,j]) + Cx2*(q[i,j] + q[i+1,j])*(u_n[i+1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j+1])*(u_n[i,j+1] - u_n[i,j])

i,j = 0,N_y
u_np1[i,j] = 2*u_n[i,j] - (u_n[i,j] - 2*dt*V_init[i,j]) + Cx2*(q[i,j] + q[i+1,j])*(u_n[i+1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j-1])*(u_n[i,j-1] - u_n[i,j])
            
i,j = N_x,0
u_np1[i,j] = 2*u_n[i,j] - (u_n[i,j] - 2*dt*V_init[i,j]) + Cx2*(q[i,j] + q[i-1,j])*(u_n[i-1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j+1])*(u_n[i,j+1] - u_n[i,j])
        
i,j = N_x,N_y
u_np1[i,j] = 2*u_n[i,j] - (u_n[i,j] - 2*dt*V_init[i,j]) + Cx2*(q[i,j] + q[i-1,j])*(u_n[i-1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j-1])*(u_n[i,j-1] - u_n[i,j])      

i = 0
u_np1[i,1:N_y -1] = 2*u_n[i,1:N_y -1] - (u_n[i,1:N_y -1] - 2*dt*V_init[i,1:N_y -1]) + Cx2*(q[i,1:N_y -1] + q[i+1,1:N_y -1])*(u_n[i+1,1:N_y -1] - u_n[i,1:N_y -1]) + Cy2*(  0.5*(q[i,1:N_y -1] + q[i,2:N_y])*(u_n[i,2:N_y] - u_n[i,1:N_y -1])  - 0.5*(q[i,0:N_y -2] + q[i,1:N_y -1])*(u_n[i,1:N_y -1] - u_n[i,0:N_y -2]) )
      
j = 0
u_np1[1:N_x -1,j] = 2*u_n[1:N_x -1,j] - (u_n[1:N_x -1,j] - 2*dt*V_init[1:N_x -1,j]) + Cx2*(  0.5*(q[1:N_x -1,j] + q[2:N_x,j])*(u_n[2:N_x,j] - u_n[1:N_x -1,j])  - 0.5*(q[0:N_x -2,j] + q[1:N_x -1,j])*(u_n[1:N_x -1,j] - u_n[0:N_x -2,j]) ) + Cy2*(q[1:N_x -1,j] + q[1:N_x -1,j+1])*(u_n[1:N_x -1,j+1] - u_n[1:N_x -1,j])

i = N_x
u_np1[i,1:N_y -1] = 2*u_n[i,1:N_y -1] - (u_n[i,1:N_y -1] - 2*dt*V_init[i,1:N_y -1]) + Cx2*(q[i,1:N_y -1] + q[i-1,1:N_y -1])*(u_n[i-1,1:N_y -1] - u_n[i,1:N_y -1]) + Cy2*(  0.5*(q[i,1:N_y -1] + q[i,2:N_y])*(u_n[i,2:N_y] - u_n[i,1:N_y -1])  - 0.5*(q[i,0:N_y -2] + q[i,1:N_y -1])*(u_n[i,1:N_y -1] - u_n[i,0:N_y -2]) )
      
j = N_y
u_np1[1:N_x -1,j] = 2*u_n[1:N_x -1,j] - (u_n[1:N_x -1,j] - 2*dt*V_init[1:N_x -1,j]) + Cx2*(  0.5*(q[1:N_x -1,j] + q[2:N_x,j])*(u_n[2:N_x,j] - u_n[1:N_x -1,j])  - 0.5*(q[0:N_x -2,j] + q[1:N_x -1,j])*(u_n[1:N_x -1,j] - u_n[0:N_x -2,j]) ) + Cy2*(q[1:N_x -1,j] + q[1:N_x -1,j-1])*(u_n[1:N_x -1,j-1] - u_n[1:N_x -1,j])


u_nm1 = u_n.copy()
u_n = u_np1.copy()
U[:,:,1] = u_n.copy()


#Process loop 
for n in range(2, N_t):
    
    #calculation at step j+1  
    #without boundary cond           
    u_np1[1:N_x,1:N_y] = 2*u_n[1:N_x,1:N_y] - u_nm1[1:N_x,1:N_y] + Cx2*(  0.5*(q[1:N_x,1:N_y] + q[2:N_x+1,1:N_y])*(u_n[2:N_x+1,1:N_y] - u_n[1:N_x,1:N_y])  - 0.5*(q[0:N_x - 1,1:N_y] + q[1:N_x,1:N_y])*(u_n[1:N_x,1:N_y] - u_n[0:N_x - 1,1:N_y]) ) + Cy2*(  0.5*(q[1:N_x ,1:N_y] + q[1:N_x,2:N_y+1])*(u_n[1:N_x,2:N_y+1] - u_n[1:N_x,1:N_y])  - 0.5*(q[1:N_x,0:N_y - 1] + q[1:N_x,1:N_y])*(u_n[1:N_x,1:N_y] - u_n[1:N_x,0:N_y - 1]) )- m[1:N_x,1:N_y]* dt * u_n[1:N_x,1:N_y]

    #Nuemann bound cond
    i,j = 0,0
    u_np1[i,j] = 2*u_n[i,j] - u_nm1[i,j] + Cx2*(q[i,j] + q[i+1,j])*(u_n[i+1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j+1])*(u_n[i,j+1] - u_n[i,j])
                
    i,j = 0,N_y
    u_np1[i,j] = 2*u_n[i,j] - u_nm1[i,j] + Cx2*(q[i,j] + q[i+1,j])*(u_n[i+1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j-1])*(u_n[i,j-1] - u_n[i,j])
                    
    i,j = N_x,0
    u_np1[i,j] = 2*u_n[i,j] - u_nm1[i,j] + Cx2*(q[i,j] + q[i-1,j])*(u_n[i-1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j-1])*(u_n[i,j-1] - u_n[i,j])
            
    i,j = N_x,N_y
    u_np1[i,j] = 2*u_n[i,j] - u_nm1[i,j] + Cx2*(q[i,j] + q[i-1,j])*(u_n[i-1,j] - u_n[i,j]) + Cy2*(q[i,j] + q[i,j-1])*(u_n[i,j-1] - u_n[i,j])
            
            
    i = 0
    u_np1[i,1:N_y -1] = 2*u_n[i,1:N_y -1] - u_nm1[i,1:N_y -1] + Cx2*(q[i,1:N_y -1] + q[i+1,1:N_y -1])*(u_n[i+1,1:N_y -1] - u_n[i,1:N_y -1]) + Cy2*(  0.5*(q[i,1:N_y -1] + q[i,2:N_y])*(u_n[i,2:N_y] - u_n[i,1:N_y -1])  - 0.5*(q[i,0:N_y -2] + q[i,j])*(u_n[i,1:N_y -1] - u_n[i,0:N_y -2]) )
                
    j = 0
    u_np1[1:N_x - 1,j] = 2*u_n[1:N_x - 1,j] - u_nm1[1:N_x - 1,j] + Cx2*(  0.5*(q[1:N_x - 1,j] + q[2:N_x,j])*(u_n[2:N_x,j] - u_n[1:N_x - 1,j])  - 0.5*(q[0:N_x - 2,j] + q[1:N_x - 1,j])*(u_n[1:N_x - 1,j] - u_n[0:N_x - 2,j]) ) + Cy2*(q[1:N_x - 1,j] + q[1:N_x - 1,j+1])*(u_n[1:N_x - 1,j+1] - u_n[1:N_x - 1,j])
            
    i = N_x
    u_np1[i,1:N_y -1] = 2*u_n[i,1:N_y -1] - u_nm1[i,1:N_y -1] + Cx2*(q[i,1:N_y -1] + q[i-1,1:N_y -1])*(u_n[i-1,1:N_y -1] - u_n[i,1:N_y -1]) + Cy2*(  0.5*(q[i,1:N_y -1] + q[i,2:N_y])*(u_n[i,2:N_y] - u_n[i,1:N_y -1])  - 0.5*(q[i,0:N_y -2] + q[i,1:N_y -1])*(u_n[i,1:N_y -1] - u_n[i,0:N_y -2]) )
            
    j = N_y
    u_np1[:,j] = u_n[:,j-1] + (CFL_2 - 1)/(CFL_2 + 1)*(u_np1[:,j-1] - u_n[:,j])
            
    
    u_nm1 = u_n.copy()      
    u_n = u_np1.copy() 
    U[:,:,n] = u_n.copy()
    
######################### PLOT #############################

anim = anim_2D(X,Y,U,dt,5,save=True)
plt.show()
