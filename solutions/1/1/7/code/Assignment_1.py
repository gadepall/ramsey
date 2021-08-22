import numpy as np
import matplotlib.pyplot as plt
from sympy.matrices import Matrix

#input points
A=np.array([-1,2])
B=np.array([-2,-2])
C=np.array([3,1])

#printing input
print("A:\n ",A)
print("B:\n ",B)
print("C:\n ",C)

# Finding the which two sides are equal
print("length AB:",np.linalg.norm(A-B))
print("length BC",np.linalg.norm(B-C))
print("length CA",np.linalg.norm(C-A))
#so After printing the result we can see that  Lenght AB and AC are same so they are same sides of the iscoseles traingle 
#FINDING THE MIDPOINT
D=np.array((B+C)/2) #it is the desired point for finding the distance from A to Side BC
# printing the midpint
print("D:\n ",D)
#Finding the distance 
print("Distance:",np.linalg.norm(D-A))
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
#plotting the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.3), A[1] * (1 + 0.01) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.003), C[1] * (1 + 0.1) , 'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0] * (1 + 0.2), D[1] * (1 + 0.13) , 'D')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

