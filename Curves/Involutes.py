import numpy as np
import matplotlib.pyplot as plt

def circle_involute(a=0,r=1,turns=1,n=1001):
    
    th = np.linspace(0,2*turns*np.pi,n)
    x = r*(np.cos(th)+(th-a)*np.sin(th))
    y = r*(np.sin(th)-(th-a)*np.cos(th))

    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.plot(x,y)


if __name__ == '__main__':
    circle_involute(a=0,turns=2)