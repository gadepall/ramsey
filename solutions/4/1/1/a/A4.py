import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
# Equation of the circle is xTx − 2(2   -1)x + 11/3 = 0
O = np.array(([2,-1])) # 
f = 3.667  # from eq we get 
r = np.sqrt(LA.norm(O)**2-f)

# function to generate circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

##Generating the circle
x_circ= circ_gen(O,r)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
print(r)

