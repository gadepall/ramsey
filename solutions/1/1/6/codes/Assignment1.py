#Assignment 1
import numpy as np
import matplotlib.pyplot as plt
from sympy.matrices import Matrix

#Points
A = np.array([-1, 2])
B = np.array([-2, -2])
C = np.array([3, 1])

#Constructing the matrix M
M = Matrix([B-A, C-A])

print(M)

#Taking the rref of the matrix M
M_rref = M.rref()
print("The rref of matrix M is : ", M_rref)

#Creating another copy of M to compute rank
M_temp = np.array([B-A, C-A])
print ("Rank of matrix M = ", np.linalg.matrix_rank(M_temp))

#Calculating the square lengths of all the sides
square_len_AB = (A - B).T @ (A - B)
square_len_BC = (B - C).T @ (B - C)
square_len_CA = (C - A).T @ (C - A)
print("Square of length of AB = ", square_len_AB)
print("Square of length of BC = ", square_len_BC)
print("Square of length of CA = ", square_len_CA)

#Checking if the triangle is isosceles or not
if (square_len_AB == square_len_BC) or (square_len_BC == square_len_CA) or (square_len_CA == square_len_AB):
    print("Isosceles triangle")
else:
    print("Not isosceles triangle")

plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.12), B[1] * (1 + 0.12) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.05), C[1] * (1 + 0.05) , 'C')
plt.plot(np.array([A[0], B[0]]),np.array([A[1], B[1]]), 'r', label="$AB$")
plt.plot(np.array([B[0], C[0]]), np.array([B[1], C[1]]),'g', label="$BC$")
plt.plot(np.array([C[0], A[0]]), np.array([C[1], A[1]]),'b', label="$CA$")
plt.grid()
plt.xlim(-3, 4)
plt.ylim(-3, 4)
plt.legend()
plt.show()
