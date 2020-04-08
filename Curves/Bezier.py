import numpy as np
import matplotlib.pyplot as plt
 
def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]


def bezier(control_points,N=101):
    """
    Bezier curves of any complexity are possible
    They interpolate between several Bezier curves, starting from lines
    Points are provided in sequence
    The first and last point are the start and end of the curve
    """
    L = control_points.copy()
    while True:
        P = []
        if len(L) == 1:
            return L[0]
        for i in range(len(L)-1):
            t = np.linspace(0,1,N)
            interp = interpolation(L[i],L[i+1],t)
            P.append(interp)

        L = P.copy()


def bezier_multi(curves,N=101):
    """
    Create points for multiple bezier curves, does not enforce a spline
    If any start or end points match the point will be doubled
    """
    
    X = []
    Y = []
    for control in curves:
        x,y = bezier(control,N)
        X += list(x)
        Y += list(y)
    
    return X,Y


def bezier_spline(curves,N=101):
    """
    Enforces a continuous spline but not smoothness
    Does not double start or end points of the component curves
    """
    
    for A,B in zip(curves[:-1],curves[1:]):
        if A[-1] != B[0]:
            raise Exception("A spline must be continuous")
    
    X = []
    Y = []
    for control in curves:
        x,y = bezier(control,N)
        X += list(x)[:-1]
        Y += list(y)[:-1]
    
    return X,Y





if __name__ == '__main__':
    x,y = bezier_spline([[(0,1),(1,1),(1,0)],
                        [(1,0),(1,-1),(0,-1)],
                        [(0,-1),(-1,-1),(-1,0)],
                        [(-1,0),(-1,1),(0,1)]
                        ],
                       N=1001)
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.plot(x,y)