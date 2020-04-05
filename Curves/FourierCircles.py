import matplotlib.pyplot as plt
import numpy as np


def linked_circles(radii,speeds,phases,time=1,n=1001,draw=True):
    
    t_vals = np.linspace(0,time*2*np.pi,n)
    
    X,Y = [],[]
    
    for t in t_vals:
        x = 0
        y = 0
        for R,S,P in zip(radii,speeds,phases):
            x += R*np.sin(t*S+(P*2*np.pi))
            y += R*np.cos(t*S+(P*2*np.pi))
        X.append(x)
        Y.append(y)
    
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


# Doesn't work at all really
def fourier_approxiation(C,num_circles,time=1,draw=True):

    t_vals = np.linspace(0,2*np.pi,len(C))
    
    def calc_coef(n,C):
        cn = C*np.exp(-1j*2*n*np.pi*t_vals)
        return sum(cn)/len(cn)

    coefs = [calc_coef(N,C) for N in range(1,num_circles+1)]
    
    R = np.absolute(coefs)
    S = np.array(range(1,num_circles+1))
    P = np.angle(coefs)
    
    print(R)
    print(S)
    print(P)
    
    linked_circles(R,S,P,time,len(C),draw=draw)





if __name__ == '__main__':
    
#    from Conversions import xy_to_complex
#    from ParametricPolygon import regular_polygon
    
    num_cos = 5
    R = [n*2-1 for n in range(num_cos,0,-1)]
    S = [(n+1)*2-1 for n in range(0,num_cos,1)]
    P = [0]*num_cos
    x,y = linked_circles(R,S,P,1,n=2001)
    
    num_cos = 4
    R = [(n*2)-1 for n in range(num_cos,0,-1)]
    S = [(n*2)-1 for n in range(0,num_cos,1)]
    P = [0]*num_cos
    x,y = linked_circles(R,S,P,1,n=2001)
    
    num_cos = 6
    R = [5**n for n in range(0,num_cos,1)]
    S = [6**n for n in range(num_cos,0,-1)]
    P = [0]*num_cos
    x,y = linked_circles(R,S,P,.5,n=4001)