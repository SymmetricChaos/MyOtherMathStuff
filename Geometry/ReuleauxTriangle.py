import numpy as np
import matplotlib.pyplot as plt
from Shapes import Circle

class ReuleauxTriangle:
    def __init__(self,r=1,pos=[0,0]):
        self.r = r
        self.pos = pos
        
    def draw(self,p=100):
        c = Circle(self.r,self.pos)

        for i in c.points(4):
            a = Circle(np.sqrt(3),i)
            a.draw(facecolor="#00000000")
        

        plt.scatter(c.points_x(4),c.points_y(4))