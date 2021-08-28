import numpy as np
from math import *
from matplotlib import pyplot as plt

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(C,r):
	len = 1000
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + C).T
	return x_circ

C1 = np.array([2,-2.5])
r1 = 3.5

C2 = np.array([2.5,-3])
r2 = sqrt(61)/2


x1= np.array([10,8])
x2= np.array([-8,-10])
x1x2 = line_gen(x1,x2)
x_circ1 = circ_gen(C1,r1)
x_circ2 = circ_gen(C2,r2)

plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')

# plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='S=0',color='g')
plt.plot(x_circ2[0,:],x_circ2[1,:],label="S'=0")

#plotting the line
plt.plot(x1x2[0,:],x1x2[1,:],'-',label='L=0',color='r')
plt.legend()