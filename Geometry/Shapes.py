import numpy as np

class Circle:
    def __init__(self,r):
        self.r = r
        self.cur = 1/r
        self.area = r*r*np.pi
    
    def draw(self,pos=[0,0],color="black"):
        ax = plt.gca()
        circ = plt.Circle(pos,radius = self.r, fc = "#00000000", ec = color)
        ax.add_patch(circ)