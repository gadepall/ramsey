import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
O = np.array(([2,1.5]))
P = np.array(([2.79,2.29]))
P_2 = np.array(([1.21,0.71]))
f = 5
r = np.sqrt(LA.norm(O)**2-f)
m = np.array(([1,-1]))
q1 = np.array(([2.79,2.29]))
q2 = np.array(([1.21,0.71]))
k1 = 0.5
k2 = -1

len = 50
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T

len = 10
dim = q1.shape[0]
x_AB = np.zeros((dim,len))
lam_1 = np.linspace(k1,k2,len)
for i in range(len):
    temp1 = q1 + lam_1[i]*m
    x_AB[:,i]= temp1.T
    O = np.array(([2,1.5]))
P = np.array(([2.79,2.29]))
P_2 = np.array(([1.21,0.71]))
f = 5
r = np.sqrt(LA.norm(O)**2-f)
m = np.array(([1,-1]))
A = np.array(([2.79,2.29]))
B = np.array(([1.21,0.71]))
k1 = 0.5
k2 = -1
len = 10
dim = q2.shape[0]
x_AC = np.zeros((dim,len))
lam_1 = np.linspace(k1,k2,len)
for i in range(len):
    temp1 = q2 + lam_1[i]*m
    x_AC[:,i]= temp1.T
plt.plot(x_AB[0,:],x_AB[1,:],label='$x=5.08 - y$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$x=1.92 - y$')
#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


coords = np.vstack((P_2,P,O)).T
plt.scatter(coords[0,:], coords[1,:])
vert_labels = ['P_1','P_2','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (coords[0,i], coords[1,i]),textcoords="offset points",xytext=(0,10), ha='center') 

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
