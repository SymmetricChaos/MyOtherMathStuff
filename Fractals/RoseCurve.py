import matplotlib.pyplot as plt
import numpy as np

def polar_to_cart(r,th):
    return r*np.cos(th), r*np.sin(th)


def rose(n,d,c=0,m=2):
    
    assert type(n) == type(d) == type(m) == int
    
    th = np.linspace(0,m*np.pi,1000)
    
    r = np.cos(n/d*th)+c
    
    x,y = polar_to_cart(r,th)

    fig = plt.figure()
    fig.set_size_inches(10,10)
    plt.axes().set_aspect("equal","datalim")
    plt.axis("off")
    plt.plot(x,y)
    plt.title(f"Rose(n={n}, d={d}, c={c})",fontsize=25)
    
    return x,y
    




if __name__ == '__main__':
    x,y = rose(5,6,0,12)