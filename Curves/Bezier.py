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
    

    bezier_example([ (-2,0), 
                     (1,-2),
                     (1.5,-1),
                     (-1,2), 
                     (1,0) ])
    
    