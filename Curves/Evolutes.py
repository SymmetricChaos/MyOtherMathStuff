import numpy as np
import matplotlib.pyplot as plt
from Normals import normals
from Envelope import envelope

# In general the evolute is the envelope of the normals
def evolute(x,y):
    m,b = normals(x,y,draw=False)
    x,y = envelope(m,b)
    

def ellipse_evolute(a,b,n=1001,draw=True):

    th = np.linspace(0,2*np.pi,n)
    x = (a*a-b*b)/a*np.cos(th)**3
    y = (b*b-a*a)/b*np.sin(th)**3
    
    if draw:
        fig = plt.figure()
        fig.set_size_inches(7,7)
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.plot(x,y)
        
    return x,y



    
    
if __name__ == '__main__':
    
    a,b = 2,1
    ellipse_evolute(a,b)
    
    th = np.linspace(0,2*np.pi,101)
    x,y = a*np.sin(th), b*np.cos(th)
    
    plt.plot(x,y)