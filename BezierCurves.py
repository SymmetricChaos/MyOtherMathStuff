# A bezier curve is the linear interpolation of several bezier curves.

import numpy as np
import matplotlib.pyplot as plt

def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]


def bezier_quadratic(begin,end,control,N=50):
    """
    The simplest interesting Bezier curve interpolates between two lines
    It is considered a quadratic curve
    """
    t = np.linspace(0,1,N)
    P0 = interpolation(begin,control,t)
    P1 = interpolation(control,end,t)
    X,Y = interpolation(P0,P1,t)
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
            interp = interpolation(L[i],L[i+1],t)
            P.append(interp)

        L = P.copy()

def bezier_string_art_quadratic(begin,end,control,N=15,color='salmon'):
    t = np.linspace(0,1,N)
    Ax, Ay = interpolation(begin,control,t)
    Bx, By = interpolation(control,end,t)
    
    for ax,bx,ay,by in zip(Ax,Bx,Ay,By):
        plt.plot([ax,bx],[ay,by],color=color)
    
    plt.plot([begin[0],control[0]],[begin[1],control[1]],color='gray')
    plt.plot([control[0],end[0]],[control[1],end[1]],color='gray')
    
    X,Y = interpolation([Ax,Ay],[Bx,By],t)
    plt.scatter(X,Y,color='black',zorder=5)
    
def bezier_string_art_cubic(begin,end,control1,control2,N=15,color='salmon'):
    t = np.linspace(0,1,N)
    Ax, Ay = interpolation(begin,control1,t)
    Bx, By = interpolation(control1,control2,t)
    Cx, Cy = interpolation(control2,end,t)
    
    Dx, Dy = interpolation([Ax,Ay],[Bx,By],t)
    Ex, Ey = interpolation([Bx,By],[Cx,Cy],t)
    
    Fx, Fy = interpolation([Dx,Dy],[Ex,Ey],t)
    
    colors = ['red','green','gray']
    for i,curves in enumerate([ [Ax,Bx,Ay,By], [Bx,Cx,By,Cy], [Dx,Ex,Dy,Ey] ]):
    
        for ax,bx,ay,by in zip(*curves):
            plt.plot([ax,bx],[ay,by],color=colors[i],zorder=-i)
        
    
    plt.scatter(Fx,Fy,color='black')
