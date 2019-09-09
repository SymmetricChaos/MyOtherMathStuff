import numpy as np
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
        self.verts = verts
        
        # links should be a dict with the relative
        # offset that defines the edge. So a value
        # of 1 indicates that the point has an edge
        # going to the next vertex in verts, while
        # a value of 2 means it has an edge going to
        # the vertex after that.
        # links = {0 : [1],
        #           1 : [1,2], 
        #           2 : [], 
        #           3 : [1],
        #           4 : []}
        
        # If links are provided follow them
        # Otherwise interpret as a chain
        if links:
            self.links = links
        else:
            self.links = dict()
            for i in range(len(verts)-1):
                self.links[i] = [1]
            self.links[len(verts)-1] = []
        
        # Check for any leaves that might
        # not have been specified and make
        # sure they are included
        for v in range(len(verts)):
            if v not in self.links.keys():
                self.links[v] = []

    
    def draw(self,color="black",**kwargs):
        for L in self.links.items():
            v = L[0]
            edges = L[1]
            for n in edges:
                plot_points([self.verts[v],self.verts[n+v]],
                            color=color,**kwargs)
    

# Place root of one tree at some vertex of
# another tree
# How to merge the tree lists correctly?
# If trees used relative offset to say where they
# link to merging them would be easy
def tree_sum(A,B,v):
    assert type(A) == Tree
    assert type(B) == Tree
    assert type(v) == int
    
    print("A")
    print(A.links)
    
    print("B")
    print(B.links)
    
    new_verts = A.verts + B.verts
    new_links = dict()
    
