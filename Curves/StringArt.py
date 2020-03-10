import matplotlib.pyplot as plt
import numpy as np

def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]

def string_bezier2(P1=[0,1],P2=[1,0],n=15,size=5):
    
    t = np.linspace(0,1,n)
    X0,Y0 = interpolation(P1,[0,0],t)
    X1,Y1 = interpolation([0,0],P2,t)
    
    
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    for x0,y0,x1,y1 in zip(X0,Y0,X1,Y1):
        plt.plot([x0,x1],[y0,y1])

string_bezier2([1,1],n=20)