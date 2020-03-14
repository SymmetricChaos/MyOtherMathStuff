import numpy as np
import matplotlib.pyplot as plt


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
    
    ellipse_evolute(1,2)