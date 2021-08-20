import math
import numpy as np
import matplotlib.pyplot as plt

# given points are P(x1,y1) and Q(x2,y2)
(x1,y1) = (-2,4)
(x2,y2) = (3,-5)

l1 = [x1,y1]
l2 = [x2,y2]

P = np.array(l1)
Q = np.array(l2)
Z = P - Q
# distance between P and Q is d.
d = np.linalg.norm(Z)
x = [l1[0], l2[0]]
y = [l1[1], l2[1]]

print("Dinstance between points P and Q is: ",d)


plt.annotate("P(-2,4)", (-2, 4))
plt.annotate("Q(3,-5)", (3, -5))
plt. plot(x,y,'-ob')
plt.xlim([-4,4])
plt.ylim([-6,6])
plt.show()

