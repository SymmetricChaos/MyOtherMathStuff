# A bezier curve is the linear interpolation of several bezier curves.

import numpy as np
import matplotlib.pyplot as plt

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
#    plt.plot(P0[0],P0[1])
##    plt.plot(P1[0],P1[1])
    X,Y = interpolation(P0,P1,t)
    return X,Y
    

def bezier(L,N=50):
    """
    Bezier curves of any complexity are possible
    They interpolate between several lines or, equivalently, between several Bezier curves
    Points are provided in sequence
    """
    Qold = L.copy()
    while True:
        P = []
        if len(Qold) == 1:
            return Qold[0]
        for i in range(len(Qold)-1):
            t = np.linspace(0,1,N)
            P.append(interpolation(Qold[i],Qold[i+1],t))

        Qold = P.copy()
        

pts = [[-2,0],[0,1.5],[.5,-1],[2,0]]
XY = bezier(pts)
plt.plot(XY[0],XY[1])
plt.scatter(pts[0][0],pts[0][1])
plt.scatter(pts[1][0],pts[1][1])
plt.scatter(pts[2][0],pts[2][1])
plt.scatter(pts[3][0],pts[3][1])