# Program to check if a given line is a tangent to the given circle or not. 
# The circle equation is x^Tx−2c^Tx+f=0 and the line equatiin is (a1 a2)x = b

from math import sqrt

def find_radius(c1,c2,f):
    radius = sqrt(c1**2 + c2**2 - f)
    return radius

def find_pdist(a1,a2,b,c1,c2):
    pdist = abs(a1*c1 + a2*c2 - b)/sqrt(a1**2 +a2**2)
    return pdist

def check_if_tangent():
    c1,c2,f = [int(x) for x in input("Enter Circle center c1,c2 and f value: ").split()] 
    radius = find_radius(c1, c2, f)
    a1,a2,b = [int(x) for x in input("Enter Line parameters a1,a2,b value: ").split()]
    perp_dist = find_pdist(a1, a2, b, c1, c2)
    if (abs(radius - perp_dist) < 1e-9): 
        print("The given line is a tangent")
    else: 
        print("The given line is not a tangent to the given circle.")

check_if_tangent()