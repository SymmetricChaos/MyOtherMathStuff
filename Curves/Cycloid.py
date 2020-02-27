import matplotlib.pyplot as plt
import numpy as np

# A cycloid is the roulette of a point on a circle as it rolls along a line

def cycloid(r=1,draw=True):
    th = np.linspace(0,2*np.pi,100)
    x = r*(th-np.sin(th))
    y = r*(1-np.cos(th))
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x,y)
        plt.title(f"Cycloid(r={r})",fontsize=25)

    return x,y


x,y = cycloid()