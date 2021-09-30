import numpy as np
a = np.array([[-2, -2, -1], [-3, 6, -1], [6, -4, -1]])
b = np.array([1, -2, 13])
x = np.linalg.solve(a, b)
print(x)
