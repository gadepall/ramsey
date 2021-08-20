import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

len = 4000
y = np.linspace(-10,10,len)
#Given hyperbola
x1 = -np.sqrt(3)*y+np.sqrt(4*(y**2)+8)
#Modified hyperbola
x2 = np.sqrt(4+y**2)

xc=[0]
yc=[0]

#Plotting the hyperbola
plt.plot(x1,y,label='Given hyperbola',color='b')
plt.plot(-x1,-y,color='b')
plt.plot(x2,y,label='Modified hyperbola',color='r')
plt.plot(-x2,-y,color='r')
plt.xlim([-10, 10])
plt.ylim([-10,10])
plt.plot(xc[0],yc[0],marker='o',color='black')
plt.axhline(0, color='black')
plt.axvline(0, color='black')

for x,y in zip(xc, yc):
    label = ' ( %d, %d )' % (x, y)
    ax.text(x, y, label)
    
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig('Figure.png')
