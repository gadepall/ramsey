import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Function for Generating a Circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Function for Generating the Lines
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

C = np.array(([4,3])) #Center of the circle
Q1 = np.array(([1,0]))  #Point of Contact Q1
Q2 = np.array(([7,6]))  #Point of Contact Q2
f = 7
r = np.sqrt(LA.norm(C)**2-f)
n = np.array(([1,1]))
m = np.array(([-1,1]))
A = np.array(([0,1]))
c1= np.array(([0,13]))
c2= np.array(([0,-1]))
k1 = -10
k2 = 10
k3 = -10
k4 = 10

#Generating the Lines
x_AB = line_dir_pt(m,A,k1,k2)       #Given Line - AB
tangent1 = line_dir_pt(m,c1,k1,k2)  #Tangent 1 - Parallel to the Given Line
normal1 = line_dir_pt(n,c2,k3,k4)   #Normal 1 - Perpendicular to AB and Tangent 1


#Generating the Circle
x_circ= circ_gen(C,r)

#Plotting the Lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB: x+y=1$', color='c')
plt.plot(tangent1[0,:],tangent1[1,:],label='$Tangent-1: x+y=13$', color='coral')
plt.plot(normal1[0,:],normal1[1,:],label='$Normal-1: x-y=-1$', color='g')

#Plotting the Circle
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle with Center C: (4,3)',color='r')

#Naming the points
tri_coords = np.vstack((Q1,Q2,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$Q_1$','$Q_2$','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, 
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points",
                 xytext=(0,10), 
                 ha='center')

#Labelling the Plots
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(fontsize='small',loc='best')
plt.grid()
plt.axis('equal')
plt.show()
