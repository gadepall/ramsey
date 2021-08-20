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
O = np.array(([5,1]))
P = np.array(([8,3]))
f = 13
r = np.sqrt(LA.norm(O)**2-f)
m = np.array(([2,-3]))
A = np.array(([8,3]))
k1 = 0.5
k2 = -1
##Generating all lines
x_AB = line_dir_pt(m,A,k1,k2)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$x=10 - (2/3)y$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


coords = np.vstack((P,O)).T
plt.scatter(coords[0,:], coords[1,:])
vert_labels = ['P','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (coords[0,i], coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()