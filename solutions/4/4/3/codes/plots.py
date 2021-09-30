  
import numpy as np
from math import *
from matplotlib import pyplot as plt

def circ_gen(C,r):
	len = 1000
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + C).T
	return x_circ

C1 = np.array([1,1])
f1 = 1
r1 = np.sqrt(np.linalg.norm(C1)**2 - f1)

C2 = np.array([1.5,-3])
f2 = -2
r2 = np.sqrt(np.linalg.norm(C2)**2 - f2)

C3 = np.array([-45/31,6/31])
f3 = -109/31
r3 = np.sqrt(np.linalg.norm(C3)**2 - f3)

x_circ1 = circ_gen(C1,r1)
x_circ2 = circ_gen(C2,r2)
x_circ3 = circ_gen(C3,r3)

plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')

# plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='S1=0',color='g')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='S2=0')
plt.plot(x_circ3[0,:],x_circ3[1,:],label='S=0')

plt.plot(-3,2,'o', color = 'red',label='Point')

plt.legend()