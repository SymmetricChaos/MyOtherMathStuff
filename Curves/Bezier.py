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


def bezier_multi(control_points,N=101):
    """
    Create points for multiple bezier curves, does not enforce a spline
    If any start or end points match the point will be doubled
    """
    
    X = []
    Y = []
    for points in control_points:
        x,y = bezier(points,N)
        X += list(x)
        Y += list(y)
    
    return X,Y


def bezier_spline(control_points,N=101):
    """
    Enforces a continuous spline but not smoothness
    Does not double start or end points of the component curves
    """
    
    for A,B in zip(control_points[:-1],control_points[1:]):
        if A[-1] != B[0]:
            raise Exception("A spline must be continuous")
    
    X = []
    Y = []
    for points in control_points:
        x,y = bezier(points,N)
        X += list(x)[:-1]
        Y += list(y)[:-1]
    
    return X,Y


def thomas_algorithm(a,b,c,r,n):
    """
    Take lists a,b,c,r and integer n
    Mutates b and r
    """
    for i in range(1,n):
        m = a[i]/b[i-1]
        b[i] = b[i] - m * c[i-1]
        r[i] = r[i] - m*r[i-1]


# Translation of algorithm from https://www.particleincell.com/2012/bezier-splines/
def bezier_spline_smooth(knots,N=101):
    """
    Enforces a smooth continuous spline
    Component curves are cubic
    Knots rather than control points are used
    The spline passes through each knot
    """
    
    for i in knots:
        if len(i) != 2:
            raise Exception("Each knot must be an (x,y) pair")
    
    # We need knots to add as vectors which numpy arrays will do
    knots = [np.array(k) for k in knots]

    n = len(knots)-1
    
    a,b,c,r = [],[],[],[]
    
    # First segment
    a = [0]
    b = [2]
    c = [1]
    r = [knots[0]+2*knots[1]]
    
    # Internal segments
    for i in range(1,n):
        a.append(1)
        b.append(4)
        c.append(1)
        r.append(4*knots[i] + 2*knots[i+1])
    
    # Final segment
    a.append(2)
    b.append(7)
    c.append(0)
    r.append(8*knots[-2] + knots[-1])
    
    # Mutate according to thomas algorithm to solve matrix
    thomas_algorithm(a,b,c,r,n)
    

    # First control point of each segment
    p1 = [0]*n
    p2 = [0]*n
    p1[n-1] = r[n-1]/b[n-1]
    for i in range(n-2,-1,-1):
        p1[i] = (r[i] - c[i] * p1[i+1])/b[i]
    
    print(n)
    print(len(p1))
    
    # Second control point of each segment    
    for i in range(0,n-1):
        p2[i] = 2*knots[i+1]-p1[i+1]
    p2[n-1] = (knots[n]+p1[n-1])/2
        
    control_points = []
    
    for k1,p1,p2,k2 in zip(knots[:-1],p1,p2,knots[1:]):
        control_points.append([k1,p1,p2,k2])
    
    
    X = []
    Y = []
    for points in control_points:
        x,y = bezier(points,N)
        X += list(x)[:-1]
        Y += list(y)[:-1]
    
    return X,Y,control_points
       




if __name__ == '__main__':
#    x,y = bezier_spline([[(0,1),(1,1),(1,0)],
#                        [(1,0),(1,-1),(0,-1)],
#                        [(0,-1),(-1,-1),(-1,0)],
#                        [(-1,0),(-1,1),(0,1)]
#                        ],
#                       N=1001)
    
    P = [[0,0],
         [1,1],
         [2,0]]
    x,y,C = bezier_spline_smooth(P)
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
#    ax.axis('off')
#    ax.set_xticks([])
#    ax.set_yticks([])
    
    plt.plot(x,y)
    plt.scatter([i[0] for i in P],[i[1] for i in P])
    for c in C:
        print(c)
        plt.scatter([i[0] for i in c],[i[1] for i in c])