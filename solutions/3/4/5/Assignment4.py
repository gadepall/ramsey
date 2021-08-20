
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
def parab_gen(y,a):
	x = y**2/a
	return x



#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-4,4,len)

#parab parameters
V = np.array(([1,-1],[-1,1]))
u = np.array(([-2*np.sqrt(2),-2*np.sqrt(2)]))
f = 4
#p = np.array(([1,0]))
#foc = np.abs(p@u)/2

O = np.array(([0,0]))
#Generating the Standard parabola

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
pcos = np.cos(np.pi/4)
psin = np.sin(np.pi/4)
P = np.array(([pcos,-psin],[psin,pcos]))
p = P[:,0]
eta = 2*u@p
#foc = np.abs(eta/D_vec[1])
foc = -eta/D_vec[1]
#print(p,foc,D_vec[1])
x = parab_gen(y,foc)
#Affine Parameters
#c1 = np.array(([-(u@V@u-2*u@u+f)/(2*u@p),0]))
#c = -P@u+c1
#print(c1)

cA = np.vstack((u+eta*p,V))
cb = np.vstack((-f,(eta*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
#c = np.array(([-2/5,7/5]))
#print(c,2/5,7/5,foc)
print(c,-5/3,1/4,foc)
c1 = np.array(([(u@V@u-2*D_vec[1]*u@u+D_vec[1]**2*f)/(eta*D_vec[1]**2),0]))
xStandardparab = np.vstack((x,y))
xActualparab = P@(xStandardparab - c1[:,np.newaxis])-u[:,np.newaxis]/D_vec[1]
xActualparab = P@xStandardparab + c[:,np.newaxis]
xstandardparab = P@xStandardparab + O[:,np.newaxis]

#Labeling the coordinates
parab_coords = np.vstack((O,c)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['$O$','$c$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#Plotting the actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Parabola',color='r')
plt.plot(xActualparab[0,:],xActualparab[1,:],label='Parabola rotated',color='b')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
