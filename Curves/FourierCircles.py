import matplotlib.pyplot as plt
import numpy as np

def fourier_circles(radii,speeds,phases,time=1,n=1001,draw=True):
    
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


#def fourier_circles_approxiation(func,num_circles,time=1,n=1001,draw=True):
#    
#    t_vals = np.linspace(0,time*2*np.pi,n)
#    v = np.array([func(t) for t in t_vals])
#    
#    def calc_coef(n,v):
#        cn = v*np.exp(-1j*2*n*np.pi*time/max(time))
#        return sum(cn)/len(cn)
#    
#
#    coefs = [calc_coef(N,v) for N in range(1,num_circles+1)]
#    
#    R = np.absolute(coefs)
#    S = np.array(range(1,num_circles+1))
#    P = np.angle(coefs)
#    
#    fourier_circles(R,S,P,time,n,draw=draw)

if __name__ == '__main__':
    
    R = [(n*2)-1 for n in range(15,0,-1)]
    S = [(n*2)-1 for n in range(1,16,1)]
    P = [0]*15
    x,y = fourier_circles(R,S,P,1,n=2001)