import numpy as np
import math
import matplotlib.pyplot as plt
from coeffs import *
#Define points P, Q and R

P = np.array([-3,-4])
Q = np.array([2,6])
R = np.array([-6,10])

#Calculate a, b and c - that is, the distances between P and Q, Q and R, P and R respectively

a = np.linalg.norm(P-Q)

b = np.linalg.norm(Q-R)

c = np.linalg.norm(P-R)


print(a)
print(b)
print(c)

d = math.sqrt((pow(a,2)+pow(b,2)))


print(d)


##Since d = c hence proved that P, Q, R make right angled triangle based on Bodhayana theorem


## Orthogonality principle

vec_X_PQ_BAR = Q-P
vec_Y_QR_BAR = R-Q
vec_Z_PR_BAR = R-P

A=P
B=Q
C=R


## Calculate XT*Y

XT = vec_X_PQ_BAR.transpose()

XTY = np.matmul(XT, vec_Y_QR_BAR)

print(XTY)

x_AB=line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label="AB")

x_BC=line_gen(B,C)
plt.plot(x_BC[0,:],x_BC[1,:],label="BC")

x_CA=line_gen(C,A)
plt.plot(x_CA[0,:],x_CA[1,:],label="CD")



plt.plot(A[0],A[1],'.')
plt.plot(B[0],B[1],'.')
plt.plot(C[0],C[1],'.')

plt.text(A[0]*(1+0.15),A[1]*(1+0.15), "A", color='red')
plt.text(B[0]*(1+0.03),B[1]*(1-0.15), "B", color='red')
plt.text(C[0]*(1+0.03),C[1]*(1+0.01), "C", color='red')


##Since XTY =0, hence proved that P, Q, R make right angled triangle based on the orthogonality principle