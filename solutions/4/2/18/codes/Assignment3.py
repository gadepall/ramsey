#Assignment 3
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#Function to generate a circle
def circleGen(O,r):
	len = 50
	theta = np.linspace(0, 2*np.pi, len)
	x_circ = np.zeros((2, len))
	x_circ[0,:] = r * np.cos(theta)
	x_circ[1,:] = r * np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Defining the points
O = np.array([3, 2])
M = np.array([4, 1])
#The end points of the resultant chord which lie on the circle
A = np.array([4 + sqrt(17), 1 + sqrt(17)])
B = np.array([4 - sqrt(17), 1 - sqrt(17)])

#Verifying if M is the midpoint of the chord
midpoint = (A + B) / 2.0
if midpoint.all() == M.all():
    print("M is the midpoint of the chord")
else:
    print("M is not the midpoint of the chord")

#Plotting the circle
x_circ = circleGen(O,6)
plt.plot(x_circ[0, :],x_circ[1, :], 'r')

#Plotting the points
plt.plot(M[0], M[1], 'o')
plt.plot(O[0], O[1], 'o')
plt.plot(A[0], A[1], 'o')
plt.plot(B[0], B[1], 'o')
plt.text(O[0], O[1] * (1 + 0.3) , 'O')
plt.text(M[0], M[1] * (1 - 1.6) , 'M')
plt.text(A[0], A[1] * (1 + 0.1) , 'A')
plt.text(B[0], B[1] * (1 + 0.3) , 'B')
#Drawing the chord which has M as the midpoint
plt.plot(np.array([A[0], B[0]]),np.array([A[1], B[1]]), 'b', label="$AB$")
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()
