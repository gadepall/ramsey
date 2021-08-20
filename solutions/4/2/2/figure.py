import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
O = np.array(([0,0]))
P = np.array(([3,2]))
Q = np.array(([-3,-2]))
f = -13
r = np.sqrt(LA.norm(O)**2-f)
m = np.array(([-2,3]))
A = np.array(([0,6]))
c1= np.array(([0, 13/2]))
c2= np.array(([0, -13/2]))
k1 =0
k2 =-2.5
k3=0.5
k4=3
##Generating all lines
x_AB = line_dir_pt(m,A,k1,k2)
tangent1 = line_dir_pt(m,c1,k1,k2)
tangent2 = line_dir_pt(m,c2,k3,k4)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$3x +2y=12$', color='c')
plt.plot(tangent1[0,:],tangent1[1,:],label='$3x+2y=13$', color='coral')
plt.plot(tangent2[0,:],tangent2[1,:],label='$3x+2y=-13$', color='g')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$',color='r')


tri_coords = np.vstack((P,Q,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.scatter(2,3, color='k')
plt.scatter(46/13,9/13,color= 'k')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
