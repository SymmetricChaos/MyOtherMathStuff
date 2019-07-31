import matplotlib.pyplot as plt
import numpy as np
from Utils.Drawing import make_canvas
from Geometry.Shapes import Circle
from Geometry.CircleIntersection import circle_intersect

def midpt(A,B):
    x = (A[0] + B[0])/2
    y = (A[1] + B[1])/2
    return [x,y]

def circle_inversion(P0,R,P):
    L = []
    for i in P:
    
        d = np.sqrt((P0[0]-i[0])**2 + (P0[1]-i[1])**2)
        
        midpt(P0,i)
        C1 = Circle(R,P0)
        C2 = Circle(d/2,midpt(P0,i))
        
        inter = circle_intersect(C1.pos,C1.r,C2.pos,C2.r)
        
        L.append(midpt(inter[0],inter[1]))
    return L


P = []
for i in np.linspace(-1,1,10):
    for j in np.linspace(-1,1,10):
        P.append([i+2.2,j])


make_canvas([-2,4],[-3,3])
C1 = Circle(1)
xy = circle_inversion(C1.pos,C1.r,P)
C1.draw()
plt.plot([i[0] for i in P],[i[1] for i in P],'ko',markersize=2)
plt.plot([i[0] for i in xy],[i[1] for i in xy],'ro',markersize=2)
plt.plot(xy[0][0],xy[0][1],P[0][0],P[0][1])
