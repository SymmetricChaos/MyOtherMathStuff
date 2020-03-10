import matplotlib.pyplot as plt
import numpy as np

def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]

def string_bezier2(P1=[0,1],P2=[1,0],n=15,size=5):
    
    t = np.linspace(0,1,n)
    L0 = interpolation(P1,[0,0],t)
    L1 = interpolation([0,0],P2,t)
    X,Y = interpolation(L0,L1,t)
    
    
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i in range(n):
        plt.plot([L0[0][i],L0[1][i]],
                 [L1[0][i],L1[1][i]])
#    plt.plot(X,Y,color="black")

string_bezier2(n=25)