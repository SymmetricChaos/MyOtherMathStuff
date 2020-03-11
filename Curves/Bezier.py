import numpy as np
import matplotlib.pyplot as plt

def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]


def bezier(control_points,N=50):
    """
    Bezier curves of any complexity are possible
    They interpolate between several Bezier curves, starting from lines
    Points are provided in sequence
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





if __name__ == '__main__':
    

    points = [[-2,0],[.5,-2],[1,2],[2,0]]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    X,Y = bezier(points)
    
    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.plot(X,Y)
    plt.scatter(xs,ys)
    for num,pos in enumerate(points):    
        plt.annotate(f"{num}: {pos}",[pos[0],pos[1]+.1])