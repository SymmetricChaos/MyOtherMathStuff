import matplotlib.pyplot as plt
import numpy as np
from SimpleCurves import polar_to_cart

def rose(n,d=1,c=0,k=1000,draw=True):
    
    assert type(n) == type(d) == type(k) == int
    
    if n%2 == 0 or d%2 == 0:
        th = np.linspace(0,2*d*np.pi,k)
    else:
        th = np.linspace(0,d*np.pi,k)
    
    r = np.cos(n/d*th)+c
    
    x,y = polar_to_cart(r,th)

    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x,y)
        if d == 1:
            plt.title(f"Rose(k={n}, c={c})",fontsize=25)
        else:
            plt.title(f"Rose(k={n}/{d}, c={c})",fontsize=25)
        
    return x,y


def maurer_rose(n,d=1,c=0,m=361,deg=10,draw=True):
    
    rad = deg*np.pi/180
    
    angs = np.array([rad*k for k in range(m)])
    
    radii = np.cos(n/d*angs)+c
    
    x,y = polar_to_cart(radii,angs)
    
    xr, yr = rose(n,d,c,draw=False)

    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x,y)
        plt.plot(xr,yr)
        if d == 1:
            plt.title(f"Rose(k={n}, c={c}, m={m}, deg={deg})",fontsize=25)
        else:
            plt.title(f"Rose(k={n}/{d}, c={c}, m={m}, deg={deg})",fontsize=25)
        
    return x,y



if __name__ == '__main__':
    x,y = rose(2,1,.3)
    maurer_rose(2,d=1,c=.3,m=361,deg=26)