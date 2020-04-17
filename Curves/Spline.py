import matplotlib.pyplot as plt
import numpy as np


def spline(parts,polys,n=1001,draw=True):
    
    end_points = []
    for lo,hi,P in zip(parts[:-1],parts[1:],polys):
        if lo >= hi:
            raise Exception("List of parts must be strictly increases")
        else:
            end_points.append((lo,hi,P))
            
    
    X = np.linspace(parts[0],parts[-1],n)
    Y = []
    for x in X:
        for lim in end_points:
            if x <= lim[1] and x >= lim[0]:
                Y.append(lim[2](x))
                break
    
    if draw == True:
        
        fig = plt.figure()
        fig.set_size_inches(12,12)
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.plot(X,Y)
        
    return X,Y


def Bspline(x,i,k,t):
    if k == 0:
        if x >= t[i] and x < t[i+1]:
            return 1
        else:
            return 0
    else:
        return (x-t[i])/(t[i+k]-t[i])*Bspline(x,i,k-1,t) + (t[i+k+1]-x)/(t[i+k+1]-t[i+1])*Bspline(x,i+1,k-1,t)


def draw_Bspline(X,i,k,t):

    y = [Bspline(x,i,k,t) for x in X]
    
    plt.plot(x,y)

if __name__ == '__main__':
    
    
#    P0 = lambda x: -1+4*x-x*x
#    P1 = lambda x: 2*x
#    P2 = lambda x: 2-x+x*x
#    
#    spline([0,1,2,3],[P0,P1,P2])
#    
#    P0 = lambda x: -2-2*x*x
#    P1 = lambda x: 1-6*x+x*x
#    P2 = lambda x: -1+x-2*x*x
#    
#    spline([0,1,2,3],[P0,P1,P2])
    
    x = np.linspace(0,3,100)
    T = [0,1,2,3]
    draw_Bspline(x,0,2,T)