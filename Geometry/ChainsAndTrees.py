import numpy as np
import copy
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



# To work as sums of chains
# Have to be a lot more complicated though
class Tree:
    def __init__(self,verts,links=None):
        for i in verts:
            assert len(i) == 2
        if len(verts) > len(links):
            raise Exception("Every vertex must have its links specified. If there are none use []")
        if len(verts) < len(links):
            raise Exception("Every vertex must have its links specified. If there are none use []")
        self.verts = copy.deepcopy(verts)
        
        
        # links should be a list with the relative
        # offset that defines the edge. So a value
        # of 1 indicates that the point has an edge
        # going to the next vertex in verts, while
        # a value of 2 means it has an edge going to
        # the vertex after that.
        # If links are provided follow them
        # Otherwise interpret as a chain
        if links:
            self.links = copy.deepcopy(links)
        else:
            self.links = [1]*(len(verts)-1)+[]
        

    def draw(self,color="black",**kwargs):
        for pos,offsets in enumerate(self.links):
            for n in offsets:
                plot_points([self.verts[pos],self.verts[pos+n]],
                            color=color,**kwargs)
        scatter_points(self.verts)
                
    def copy(self):
        return Tree(copy.deepcopy(self.verts),copy.deepcopy(self.links))


    def shift(self,x=0,y=0):
        """Shift position"""
        self.verts = [[i[0]+x,i[1]+y] for i in self.verts]
    

# Place root of one tree at some vertex of
# another tree
# How to merge the tree lists correctly?
# If trees used relative offset to say where they
# link to merging them would be easy
def tree_sum(A,B,v):
    assert type(A) == Tree
    assert type(B) == Tree
    assert type(v) == int
    
    A = A.copy()
    B = B.copy()
    
    A.shift(B.verts[v][0]-A.verts[0][0],
            B.verts[v][1]-A.verts[0][1])
    
    new_verts = B.verts + A.verts[1:]
    new_links = B.links + A.links[1:]
    
    print(new_links)
    print(new_links[v])
    new_links[v].append(len(A.links)-v)
    print(new_links)
    
    return Tree(new_verts,new_links)
    
