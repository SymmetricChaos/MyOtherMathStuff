import matplotlib.pyplot as plt
import numpy as np

def simple_rose(k):
    
    if k % 2 == 0:
        pts = np.linspace(0,2*np.pi,1000)
    else:
        pts = np.linspace(0,np.pi,1000)
    
    
    x = np.cos(pts*k)*np.cos(pts)
    y = np.cos(pts*k)*np.sin(pts)
    
    return x,y



if __name__ == '__main__':
    x,y = simple_rose(3)
    
    fig = plt.figure()
    fig.set_size_inches(10,10)
    plt.axes().set_aspect("equal","datalim")
    plt.axis("off")
    plt.plot(x,y)