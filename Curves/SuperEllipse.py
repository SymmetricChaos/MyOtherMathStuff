import matplotlib.pyplot as plt
import numpy as np


def superformula(m = 0, n1 = 1, n2 = 1, n3 = 1, r = 1, turns = 1, n = 1001):
    
    th = np.linspace(0,2*turns*np.pi,n)
    
    aux1 = np.absolute(np.cos((m*th)/4)/r)**n2
    aux2 = np.absolute(np.sin((m*th)/4)/r)**n3
    raux = (aux1+aux2)**(-1/n1)
    x = raux*np.cos(th)
    y = raux*np.sin(th)
    
    return x,y





if __name__ == '__main__':
        
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    x,y = superformula(5,.5,.2,8)
    
    plt.plot(x,y)