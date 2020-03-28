import matplotlib.pyplot as plt
import numpy as np

# https://web.archive.org/web/20171208231427/http://ftp.lyx.de/Lectures/SuperformulaU.pdf


def superformula(a=1, b=1, m1=0, m2=0, n1=1, n2=1, n3=1, turns = 1, n = 1001):
    
    th = np.linspace(0,2*turns*np.pi,n)
    
    
    cos_vals = np.cos((m1*th)/4)
    sin_vals = np.sin((m2*th)/4)
    
    aux1 = np.absolute(cos_vals/a)**n2
    aux2 = np.absolute(sin_vals/b)**n3
    raux = (aux1+aux2)**(-1/n1)
    x = raux*np.cos(th)
    y = raux*np.sin(th)
    
    return x,y





if __name__ == '__main__':
        
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
#    ax.axis('off')
#    ax.set_xticks([])
#    ax.set_yticks([])
    
    x,y = superformula(a=1,b=1,n2=1,n3=1,n1=-20,m1=88,m2=64,turns=1)
    
    plt.plot(x,y)