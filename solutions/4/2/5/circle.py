#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
R=2
n=65
t=np.linspace(0,2*np.pi,n+1)
x=R+R*np.cos(t)
y=R+R*np.sin(t)
plt.axis("equal")
plt.annotate("0,a",(0,2))
plt.annotate("a,0",(2,0))
plt.grid()
plt.plot(x,y)
plt.show()


# In[ ]:





# In[ ]:




