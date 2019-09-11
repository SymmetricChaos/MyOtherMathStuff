import copy
from Utils.Drawing import scatter_points, plot_points

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


    def draw_verts(self):
        scatter_points(self.verts)


    def copy(self):
        """Proper deep copy"""
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
    new_links[v].append(len(A.links)-v)
    
    return Tree(new_verts,new_links)
    
