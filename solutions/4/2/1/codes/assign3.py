import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
def circ_gen(c,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + c).T
	return x_circ

c = np.array(([5/2,-1]))
a = np.array(([-1,2]))
b=np.array(([0,0]))
d = np.array(([3,-4]))

f = -5
r = np.sqrt(LA.norm(c)**2-f)
print (r)
##Generating the circle
x_circ= circ_gen(c,r)



#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


tri_coords = np.vstack((a,b,c,d)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['a','b','c','d']
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
plt.show()
