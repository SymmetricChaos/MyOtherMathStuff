import matplotlib.pyplot as plt
import numpy as np
from numpy import pi,cos,sin

def regular_polygon(sides,r=1,n=1001,draw=True):
    th = np.linspace(0,1,n)
    
    a = np.cos(np.pi/sides)
    b = np.cos(2*np.pi*((sides*th)%1)/sides-np.pi/sides)
    h = a/b
    
    x = r*h*cos(2*pi*th)
    y = r*h*sin(2*pi*th)
    
    if draw == True:
        
        fig = plt.figure()
        fig.set_size_inches(12,12)
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.scatter(x,y)
        
    return x,y


if __name__ == '__main__':
    
    x,y = regular_polygon(11,n=301)
