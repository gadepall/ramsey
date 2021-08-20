import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(-8,7,100)
n = np.array([2,5])    #directional vector  n = np.array([a, b])
A = np.array([-7,3])   #given first vector
B = np.array([5,-11])  #given second vector
                        #X = np.array([x,y])   vector line passing through
                        # equation of line n^T X  = c 
                        # parellel so directional vector will be same for both
M = (A + B)/2           # passing through mid point of A and B
c = np.dot(n, M)        # M will satisfy that equation
print('M = ', M)
print(c)

# equation of line 
# y = (-a/b)*x + c/b

y1 = (-2/5)*x + 11/5
y2 = (-2/5)*x + c/5
x3 = [A[0], B[0], M[0]]
y3 = [A[1], B[1], M[1]]

plt.plot(x3,y3,'-oy')
plt.plot(x, y1, label='(2 5)x = 11')
plt.plot(x, y2, label='(2 5)x = -22')
plt.annotate("A(-7,3)", (-7,3))
plt.annotate("B(5,-11)", (5, -11))
plt.annotate("M(-1,-4)", (-1, -4))
plt.xlim(-8, 7)
plt.ylim(-15, 10)
plt.legend(loc='upper right')
plt.show()
