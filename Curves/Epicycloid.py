import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd

def epicycloid(incirc,outcirc,draw=True):
    
    R, r = incirc, outcirc
    g = gcd(R,r)
    R, r = R//g, r//g
    s = r+R
    
    th = np.linspace(0,R*r*np.pi,1000)
    
    x = s*np.cos(th) - r*np.cos(s/r*th)
    y = s*np.sin(th) - r*np.sin(s/r*th)
    
    th = np.linspace(0,2*np.pi,1000)
    x_circ = np.cos(th)*R
    y_circ = np.sin(th)*R
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x_circ,y_circ,color="black")
        plt.plot(x,y,color="CornflowerBlue")
        plt.title(f"Epicycloid(R={R},r={r})",fontsize=25)

    return x,y


x,y = epicycloid(3,1)
x,y = epicycloid(1,2)
x,y = epicycloid(3,2)
x,y = epicycloid(2,3)