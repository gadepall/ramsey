import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Generating points on a circle
def circ_gen(O,r):
	len = 100
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

O = np.array([-4,1])
R = np.sqrt(2)/2
circle = circ_gen(O,R)
plt.plot(circle[0,:],circle[1,:])
plt.axis('equal')
plt.text(-4,1,'. (-4,1)',fontsize=10,color='red')
plt.hlines(y=0, xmin=-5.5,xmax=0.5,color='black')
plt.vlines(x=0, ymin=-1,ymax=3,color='black')

plt.savefig('circle.png')
