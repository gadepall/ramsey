import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

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

#parameters for circle
f = 18
c = np.array(([3.5,2.5])) #centre of circle
r = np.sqrt(LA.norm(c)**2 - f) #radius of circle

#parameters for tangent
m = np.array(([1,-1])) #direction vector for tangent

#points of contact

q1x = 4
q1y = 3
Q1 = np.array(([q1x,q1y]))
q2x = 3
q2y = 2
Q2 = np.array(([q2x,q2y]))

#kappa value
k1 = -1
k2 = 1

x_AB = line_dir_pt(m,Q1,k1,k2)
x_BC = line_dir_pt(m,Q2,k1,k2)

#Generating the circle
x_circ= circ_gen(c,r)

plt.figure(figsize=(8,8))

#Plotting the circle and \ is needed before space to print space in the label
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle\ with\ centre\ c(3.5,2.5)$')
#Plotting tangents
plt.plot(x_AB[0,:],x_AB[1,:],label='$Tangent1 : (1\ 1)x = 7$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$Tangent2 : (1\ 1)x = 5$')

#Labeling the coordinates
tri_coords = np.vstack((Q1,Q2,c)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['Q1','Q2','c']
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
