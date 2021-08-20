import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
O = np.array(([13/2,13/2])) # found from eq
A = np.array(([2,3])) # passing through Point 1
B = np.array(([5,1])) # passing through Point 2
C= np.array(([3,2])) # # passing through Point 3 
f = 52  # solved from equation
r = np.sqrt(LA.norm(O)**2-f)

# function to generate circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

##Generating the circle
x_circ= circ_gen(O,r)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

tri_coords = np.vstack((A,B,C,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A(2,3)','B(5,1)','C(3,2)','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
