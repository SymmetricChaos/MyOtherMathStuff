import numpy as np
import matplotlib.pyplot as plt
from Utils.Drawing import scatter_points, plot_points

## Basically just a polygon that isn't closed
class Chain:
    def __init__(self,verts):
        if len(verts) < 2:
            raise Exception("Not a chain.")
        for i in verts:
            assert len(i) == 2
        self.verts = verts


    def draw(self,color="black",**kwargs):
        """Draw the chain"""
        plot_points(self.verts,color=color,**kwargs)
        

    def draw_points(self,color="black",**kwargs):
        """Draw the vertices of the chain"""
        scatter_points(self.verts,color=color,**kwargs)


    def copy(self):
        """Create an identical Chain"""
        return Chain(self.verts[:])


    def _length(self):
        """Length of the chain"""
        V = self.verts
        total = 0
        for pos in range(len(V)-1):
            A = V[pos]
            B = V[pos+1]
            xdiff = A[0] - B[0]
            ydiff = A[1] - B[1]
            total += np.sqrt(xdiff**2 + ydiff**2)
        return total
    
    
    def _x(self):
        """x-coordinates of the vertices"""
        return [i[0] for i in self.verts]


    def _y(self):
        """y-coordinates of the vertices"""
        return [i[1] for i in self.verts]


    def shift(self,x=0,y=0):
        """Shift position"""
        self.verts = [[i[0]+x,i[1]+y] for i in self.verts]


    # Properties to make access more intuitive
    length = property(_length)
    x = property(_x)
    y = property(_y)
        