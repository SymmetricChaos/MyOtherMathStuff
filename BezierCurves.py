# A bezier curve is the linear interpolation of several bezier curves.

import numpy as np
import matplotlib.pyplot as plt
from Utils import make_canvas

def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]


def bezier_quadratic(begin=[0,0],end=[0,0],control=[0,0],N=50):
    """
    The simplest interesting Bezier curve interpolates between two lines
    It is considered a quadratic curve
    """
    t = np.linspace(0,1,N)
    P0 = interpolation(begin,control,t)
    P1 = interpolation(control,end,t)
    X,Y = interpolation(P0,P1,t)
#    plt.plot(P0[0],P0[1])
#    plt.plot(P1[0],P1[1])
#    plt.plot(X,Y)
    return X,Y
    

def bezier(begin,end,control,N=50):
    """
    Bezier curves of any complexity are possible
    They interpolate between several lines or, equivalently, between several Bezier curves
    Points are provided in sequence
    """
    L = [begin] + control + [end]
    while True:
        P = []
        if len(L) == 1:
            return L[0]
        for i in range(len(L)-1):
            t = np.linspace(0,1,N)
            P.append(interpolation(L[i],L[i+1],t))

        L = P.copy()
        

fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5])

pts = [[0,1.5],[.5,-1]]

X,Y = bezier([-2,0],[2,0],pts)

plt.plot(X,Y)

plt.scatter(pts[0][0],pts[0][1],color='k')
plt.scatter(pts[1][0],pts[1][1],color='k')
