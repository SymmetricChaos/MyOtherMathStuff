import matplotlib.pyplot as plt
import numpy as np

def epicycloid(n,d,draw=True):
    th = np.linspace(0,12*n*np.pi,1000)
    
    k = n/d
    
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
        plt.title(f"Epicycloid(k={n}/{d})",fontsize=25)

    return x,y


x,y = epicycloid(3,1)
x,y = epicycloid(2,3)