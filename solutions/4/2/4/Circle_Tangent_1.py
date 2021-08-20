# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:59:56 2020

@author: sandh
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '..\CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from conics.funcs import circ_gen


#Input parameters'''
f = 8
P = np.array(([2,2]))
m = np.array(([1,1]))
m2= np.array(([1,-1]))
O = np.array(([3,1]))
Q = np.array(([0,0]))
k1 = 2
k2 = -2.5
x_AB = line_dir_pt(m,P,k1,k2)
x_BC = line_dir_pt(m2,Q,k1,k2)

r = np.sqrt(LA.norm(O)**2-f)
##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$Tangent: m=1 $')
plt.plot(x_BC[0,:],x_BC[1,:],label='$Line2:  m=-1 $')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


#Labeling the coordinates

tri_coords = np.vstack((P,Q,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.grid() # minor
plt.axis('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')


plt.savefig('./CircleTangent.jpg')
plt.show()