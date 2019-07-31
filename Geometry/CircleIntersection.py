import matplotlib.pyplot as plt
import numpy as np

def circle_intersect(p1,r1,p2,r2,dots=False):
    R = np.sqrt((p1[0]-p2[0])**2 +
                (p1[1]-p2[1])**2)
    
    if R > r1+r2:
        return None
    
    s = np.sqrt(2 * (r1*r1 + r2*r2) / (R**2) - ((r1*r1-r2*r2)**2) / (R**4) - 1)
    a = (r1*r1 - r2*r2) / (2*R*R)
    gx = s*(p2[1]-p1[1])/2
    gy = s*(p1[0]-p2[0])/2
    
    fx = (p1[0]+p2[0]) / 2 + a * (p2[0]-p1[0])
    fy = (p1[1]+p2[1]) / 2 + a * (p2[1]-p1[1])
    
    if dots == True:
        plt.plot(fx+gx,fy+gy,'bo')
        plt.plot(fx-gx,fy-gy,'bo')
    
    return [fx+gx,fy+gy],[fx-gx,fy-gy]

def midpt(A,B):
    x = (A[0] + B[0])/2
    y = (A[1] + B[1])/2
    return [x,y]

