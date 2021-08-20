import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Input parameters
O = np.array(([2,3]))
P = np.array(([7,4]))
Q = np.array(([2,4]))
f = 12
r = np.sqrt(LA.norm(O)**2-f)

##Generating the circle
x_circ= circ_gen(O,r)

a= (np.array(([O,P,Q,O]))).T
plt.plot((a[0,:]),(a[1,:]))

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

#Labeling the coordinates
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
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

