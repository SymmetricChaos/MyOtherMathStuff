import matplotlib.pyplot as plt
import numpy as np

def fourier_circles(radii,speeds,phases,time,n=1001,draw=True):
    
    time = np.linspace(0,time*2*np.pi,n)
    
    X,Y = [],[]
    
    for t in time:
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

if __name__ == '__main__':
    
    x,y = fourier_circles([1,2,1],[2,3,7],[0,-.5,.5],1,n=2001)