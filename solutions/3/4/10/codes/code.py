import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)
#ellipsegeneration
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#Ellipse parameters
V = np.array(([41,12],[12,34]))
u = np.array(([0,0]))
f = -75
c = -LA.inv(V)@u
#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
pcos = np.cos(np.pi/4)
psin = np.sin(np.pi/4)
P = np.array(([pcos,-psin],[psin,pcos]))
a = np.sqrt(-f/D_vec[0])
b = np.sqrt(-f/D_vec[1])
xStandardEllipse = ellipse_gen(a,b)

#Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#Affine transform 
xActualEllipse = P@xStandardEllipse
MajorActual = P@MajorStandard
MinorActual = P@MinorStandard

#

#Plotting the standard ellipse
plt.plot(xStandardEllipse[0,:],xStandardEllipse[1,:],label='Transformed ellipse')

#Plotting the actual ellipse
plt.plot(xActualEllipse[0,:],xActualEllipse[1,:],label='Given ellipse')

#Labeling the coordinates
tri_coords = np.vstack((MajorStandard,MinorStandard,MajorActual,MinorActual,c)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$a$','$b$','$a^{\prime}$','$b^{\prime}$','$\mathbf{c}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')
plt.show()

