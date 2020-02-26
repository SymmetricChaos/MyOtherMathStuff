import matplotlib.pyplot as plt
import numpy as np

def polar_to_cart(r,th):
    return r*np.cos(th), r*np.sin(th)


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
        plt.title(f"MaurerRose(k={n}/{d},m={m},d={deg})",fontsize=25)
        
    return x,y



if __name__ == '__main__':
    x,y = rose(4,7,1)
    maurer_rose(6,d=5,c=1,m=1061,deg=71)