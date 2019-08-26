import numpy as np
import matplotlib.pyplot as plt

class SuperEllipse:
    def __init__(self,a=1,b=1,n=.5,pos=[0,0]):
        if b > a:
            a,b = b,a
        self.a = a
        self.b = b
        self.n = n
        self.pos = pos
        
    def draw(self,p=100):
        th = np.linspace(0,np.pi,p)
        print()
        x = self.a*np.cos(th)**(2/self.n)
        y = self.b*np.sin(th)**(2/self.n)
        
#        X = np.append(x,[-x])
#        Y = np.append(y,[-y])
#
#        plt.plot(X[1:],Y[1:],color='black')

        plt.plot(x,y)
        plt.plot(-x,-y)