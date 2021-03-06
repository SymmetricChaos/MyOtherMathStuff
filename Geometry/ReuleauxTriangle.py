import numpy as np
import matplotlib.pyplot as plt
from Shapes import Circle
from Utils.Drawing import make_canvas


class ReuleauxTriangle:
    def __init__(self,r=1,pos=[0,0]):
        self.r = r
        self.pos = pos
        
    def draw(self,p=100):
        c = Circle(self.r,self.pos)
        r = np.sqrt(3)
        
        for i in c.points(4)[:3]:
            a = Circle(r,i)
            a.draw(facecolor="#00000000")
        

        plt.scatter(c.points_x(4),c.points_y(4))
        
A = ReuleauxTriangle()

make_canvas([-3,3],size=4)
A.draw()