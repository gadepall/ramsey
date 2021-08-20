#Ritesh_Kumar


import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
def circ_gen(O,r):
	len = 100
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
O1 = np.array(([1,1]))
O2 = np.array(([5,5]))
r1 = 1
r2 = 5
##Generating the circle
x_circ1= circ_gen(O1,r1)
x_circ2= circ_gen(O2,r2)
#Plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$',color='r')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle2$',color='b')
##plt.annotate(" O1", (5,5))
##plt.annotate("O2", (1,1))
plt.annotate(" P1(1,2)", (1,2))
##plt.scatter(5,5,color= 'b')
##plt.scatter(1,1,color= 'r')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
