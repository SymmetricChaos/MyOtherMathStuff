import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd

def epicycloid(n,d,draw=True):
    
    g = gcd(n,d)
    n, d = n//g, d//g
    k = n/d
    
    th = np.linspace(0,n*d*np.pi,1000)
    
    x = (k+1)*np.cos(th) - np.cos((k+1)*th)
    y = (k+1)*np.sin(th) - np.sin((k+1)*th)
    
    x_circ = np.cos(th)*k
    y_circ = np.sin(th)*k
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x,y)
        plt.plot(x_circ,y_circ)
        if d == 1:
            plt.title(f"Epicycloid(k={n})",fontsize=25)
        else:
            plt.title(f"Epicycloid(k={n}/{d})",fontsize=25)

    return x,y


x,y = epicycloid(5,1)
x,y = epicycloid(4,3)