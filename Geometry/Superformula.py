import numpy as np
import matplotlib.pyplot as plt

class Superellipse:
    def __init__(self,m=0,n1=1,n2=1,n3=1,r=1,pos=[0,0]):
        self.m = m
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.r = r
        self.pos = pos
    
    def draw(self,th):
        aux1 = np.absolute(np.cos((self.m*th)/4)/self.r)**self.n2
        aux2 = np.absolute(np.sin((self.m*th)/4)/self.r)**self.n3
        raux = (aux1+aux2)**(-1/self.n1)
        x = raux*np.cos(th)
        y = raux*np.sin(th)
        plt.plot(x,y)