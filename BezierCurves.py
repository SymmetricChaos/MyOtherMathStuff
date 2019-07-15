# A bezier curve is the linear interpolation of several bezier curves.


import numpy as np
import matplotlib.pyplot as plt
from Utils import make_canvas

def interpolation(X,Y,p):
    """The point that is some exactly p percent of the wat between x and y"""
    x = X[0]*(1-p) + X[1]*p
    y = Y[0]*(1-p) + Y[1]*p
    return [x,y]

#def bezierQuad(begin=[0,0],end=[0,0],control=[0,0]):
#    
#    t = np.linspace(0,1,50)
#    P0 = perpt(beg[0],beg[1],control[0],control[1],t)
#    P1 = perpt(control[0],control[1],end[0],end[1],t)
#    
#    X,Y = perpt(P0[0],P0[1],P1[0],P1[1],t)
#    
#    fig, ax = make_canvas([-3,3],[-3,3],size=[7,7])
#    
#    plt.plot(X,Y,lw=5,color='black')
#    plt.plot([beg[0],end[0],control[0]],[beg[1],end[1],control[1]],'ko')
#    
#    plt.plot([P0[0][20],P1[0][20]],
#             [P0[1][20],P1[1][20]],color='red',lw=2)
#    plt.plot([P0[0][25],P1[0][25]],
#             [P0[1][25],P1[1][25]],color='red',lw=2)
#    plt.plot([P0[0][30],P1[0][30]],
#             [P0[1][30],P1[1][30]],color='red',lw=2)
#    plt.plot([beg[0],control[0],end[0]],[beg[1],control[1],end[1]],
#             zorder = 0, color = 'blue')
#    plt.title("Quadratic Bezier Curve")


def bezier_quadratic(begin=[0,0],end=[0,0],control=[0,0],N=50):
    """
    The simplest interesting Bezier curve interpolates between two lines
    It is considered a quadratic curve
    """
    t = np.linspace(0,1,N)
    P0 = interpolation(begin,control,t)
    P1 = interpolation(control,end,t)
    
    X,Y = interpolation(P0,P1,t)
    return X,Y
    

def bezier(L,N=50):
    """
    Bezier curves of any complexity are possible
    They interpolate between several lines or, equivalently, between several Bezier curves
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
        

pts = [[-2.5,-1.5],[-1,2],[0,-5],[-2,3],[5,1]]
XY = bezier(pts)
plt.plot(XY[0],XY[1])
plt.scatter(pts[0][0],pts[0][1])
plt.scatter(pts[1][0],pts[1][1])
plt.scatter(pts[2][0],pts[2][1])
plt.scatter(pts[3][0],pts[3][1])
plt.scatter(pts[4][0],pts[4][1])
plt.scatter(pts[5][0],pts[5][1])