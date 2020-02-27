import matplotlib.pyplot as plt
import numpy as np

def epicycloid(k=1,draw=True):
    th = np.linspace(0,4*np.pi,1000)
    
    x = (k+1)*np.cos(th) - np.cos((k+1)*th)
    y = (k+1)*np.sin(th) - np.sin((k+1)*th)
    
    x_circ = np.cos(th)
    y_circ = np.sin(th) 
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x,y)
        plt.plot(x_circ,y_circ)
        plt.title(f"Epicycloid(k={k})",fontsize=25)

    return x,y


x,y = epicycloid(k=1)