# A bezier curve is the linear interpolation of several bezier curves.


import numpy as np
import matplotlib.pyplot as plt
from Utils import make_canvas

def interpolation(x1,y1,x2,y2,p):
    """The point that is some exactly p% of the wat between x and y"""
    x = (x1)*(1-p) + (x2)*(p)
    y = (y1)*(1-p) + (y2)*(p)
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
    The simplest interesting Bezier curve is quadratic
    It interpolates between two lines to creates a curve
    """
    t = np.linspace(0,1,N)
    P0 = interpolation(begin[0],begin[1],control[0],control[1],t)
    P1 = interpolation(control[0],control[1],end[0],end[1],t)
    
    X,Y = interpolation(P0[0],P0[1],P1[0],P1[1],t)
    
    

def bezier(L):
    """
    Bezier curves of any complexity are possible
    They interpolate between several lines (or between several Bezier curves)
    """
    Qold = L.copy()
    while True:
        P = []
        if len(Qold) == 1:
            return Qold
        for i in range(len(Qold)-1):
            t = np.linspace(0,1,50)
            P.append(interpolation(Qold[i][0],Qold[i][1],Qold[i+1][0],Qold[i+1][1],t))

        Qold = P.copy()
        
pts = [[-2.5,-1.5],[-1,2],[0,-5],[-2,3],[5,1],[2.5,-1.5]]
XY = bezier(pts)

print(pts)

print(interpolation(0,0,1,1,.5))