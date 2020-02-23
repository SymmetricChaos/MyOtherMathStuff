import matplotlib.pyplot as plt
import numpy as np

def simple_rose(k):
    
    assert type(k) == int
    
    if k % 2 == 0:
        pts = np.linspace(0,2*np.pi,1000)
    else:
        pts = np.linspace(0,np.pi,1000)
    
    
    x = np.cos(pts*k)*np.cos(pts)
    y = np.cos(pts*k)*np.sin(pts)
    
    return x,y

def rational_rose(n,d):
    
    assert type(n) == type(d) == int
    pts = np.linspace(0,7*np.pi,1000)
    
    x = np.cos(pts*n/d)*np.cos(pts)
    y = np.cos(pts*n/d)*np.sin(pts)
    
    return x,y

if __name__ == '__main__':
#    x,y = simple_rose(3)
    x,y = rational_rose(3,7)
    
    fig = plt.figure()
    fig.set_size_inches(10,10)
    plt.axes().set_aspect("equal","datalim")
    plt.axis("off")
    plt.plot(x,y)
    
    