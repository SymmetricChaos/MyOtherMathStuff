import numpy as np
import matplotlib.pyplot as plt


def superformula(th, m = 0, n1 = 1, n2 = 1, n3 = 1, r = 1):
    aux1 = np.absolute(np.cos((m*th)/4)/r)**n2
    aux2 = np.absolute(np.sin((m*th)/4)/r)**n3
    raux = (aux1+aux2)**(-1/n1)
    x = raux*np.cos(th)
    y = raux*np.sin(th)
    
    return x,y

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,xlim=(-2, 2), ylim=(-2, 2))

th = np.arange(0,2*np.pi,.01)
th = np.append(th,0)


x, y = superformula(th,1,1,.5,.5,.5)

ax.plot(x, y, lw=2)