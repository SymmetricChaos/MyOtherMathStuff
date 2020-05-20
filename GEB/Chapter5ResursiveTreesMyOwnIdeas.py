import Utils.Drawing as draw
import numpy as np

# Complex recursive tree

def Graph1(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]-5*s , root[1]+1 ]
    leaf1 = [ root[0]+5*s , root[1]+1 ]
    leaf2 = [ root[0]-5*s , root[1]+2 ]
    
    draw.draw_circle_p(node1,R=.06,ax=ax)
    draw.draw_circle_p(node2,R=.06,ax=ax)
    draw.connect_p(node1,node2,linewidth=1)
    draw.connect_p(node2,leaf2,linewidth=1)
    draw.connect_p(node1,leaf1,linewidth=1)

    return leaf1,leaf2

def Graph2(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]+5*s , root[1]+1 ]
    leaf1 = [ root[0]-5*s , root[1]+1 ]
    leaf2 = [ root[0]+5*s , root[1]+2 ]
    
    draw.draw_circle_p(node1,R=.06,ax=ax)
    draw.draw_circle_p(node2,R=.06,ax=ax)
    draw.connect_p(node1,node2,linewidth=1)
    draw.connect_p(node1,leaf1,linewidth=1)
    draw.connect_p(node2,leaf2,linewidth=1)

    return leaf1,leaf2

def Graph3(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]+5*s , root[1]+1 ]
    node3 = [ root[0]-5*s , root[1]+1 ]
    leaf1 = [ root[0]+5*s , root[1]+2 ]
    leaf2 = [ root[0]-5*s , root[1]+2 ]
    
    draw.draw_circle_p(node1,R=.06,ax=ax)
    draw.draw_circle_p(node2,R=.06,ax=ax)
    draw.draw_circle_p(node3,R=.06,ax=ax)
    
    draw.connect_p(node1,node2,linewidth=1)
    draw.connect_p(node1,node3,linewidth=1)
    draw.connect_p(node2,leaf1,linewidth=1)
    draw.connect_p(node3,leaf2,linewidth=1)

    return leaf1,leaf2

def Graph4(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    leaf1 = [ root[0]+5*s , root[1]+1 ]
    leaf2 = [ root[0]-5*s , root[1]+1 ]
    
    draw.draw_circle_p(node1,R=.06,ax=ax)
    
    draw.connect_p(node1,leaf1,linewidth=1)
    draw.connect_p(node1,leaf2,linewidth=1)

    return leaf1,leaf2

GDict = {1:Graph1, 
         2:Graph2, 
         3:Graph3,
         4:Graph4}
        

def recur(graph,root,levels=1,scale=0,ax=None):
    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = graph(root,scale,ax)
        l,r = np.random.choice([1,1,2,2,3,4],2)
        recur(GDict[l],leaf1,levels,scale+1,ax)
        recur(GDict[r],leaf2,levels,scale+1,ax)


def RandomTreeExample():
    draw.make_blank_canvas([-10,10],[-5,15],[14,14])
    base, = np.random.choice([1,2,3,4],1)
    recur(GDict[base],[0,-2],6)
    draw.title("Randomized Tree",size=22)
    # Show the components
    draw.draw_rect_xy(-5,11.5,-3,14.5,ec='black',fc='white',zorder=-1)
    Graph1([-4,12],3)
    draw.draw_rect_xy(3,11.5,5,14.5,ec='black',fc='white',zorder=-1)
    Graph2([4,12],3)
    draw.draw_rect_xy(-2.5,11.5,-.5,14.5,ec='black',fc='white',zorder=-1)
    Graph3([-1.5,12],3)
    draw.draw_rect_xy(.5,11.5,2.5,14.5,ec='black',fc='white',zorder=-1)
    Graph4([1.5,12],3)

    
if __name__ == '__main__':
    
    RandomTreeExample()
    draw.show_now()