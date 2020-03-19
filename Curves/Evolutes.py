import numpy as np
import matplotlib.pyplot as plt
from Normals import normals
from Envelope import envelope
from SimpleCurves import ellipse

# In general the evolute is the envelope of the normals
def evolute(x,y,draw=True):
    m,b = normals(x,y,draw=False)
    x,y = envelope(m,b,draw=draw)
    return x,y
    

# The specific evolute of an ellipse
def ellipse_evolute(a,b,n=1001,color="blue",alpha=1,draw=True):

    th = np.linspace(0,2*np.pi,n)
    x = (a*a-b*b)/a*np.cos(th)**3
    y = (b*b-a*a)/b*np.sin(th)**3
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(7,7)
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.plot(x,y,color=color,alpha=alpha)
        
    return x,y



    
    
if __name__ == '__main__':
    
    
    x1,y1 = ellipse(2,1,n=501)
    x2,y2 = evolute(x1,y1,draw=False)
    
    m,b = normals(x1,y1,color="salmon",alpha=.05)
    
    plt.plot(x1,y1)
    plt.plot(x2,y2,color="black")
    