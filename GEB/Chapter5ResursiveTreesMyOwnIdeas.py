import Utils.Drawing as draw
import numpy as np

# Complex recursive tree

def F_graph1(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]-5*s , root[1]+1 ]
    leaf1 = [ root[0]+5*s , root[1]+1 ]
    leaf2 = [ root[0]-5*s , root[1]+2 ]
    
    draw.draw_circle_p(node1,R=.1,ax=ax)
    draw.draw_circle_p(node2,R=.1,ax=ax)
    draw.connect_p(node1,node2)
    draw.connect_p(node2,leaf2)
    draw.connect_p(node1,leaf1)

    return leaf1,leaf2

def F_graph2(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]+5*s , root[1]+1 ]
    leaf1 = [ root[0]-5*s , root[1]+1 ]
    leaf2 = [ root[0]+5*s , root[1]+2 ]
    
    draw.draw_circle_p(node1,R=.1,ax=ax)
    draw.draw_circle_p(node2,R=.1,ax=ax)
    draw.connect_p(node1,node2)
    draw.connect_p(node1,leaf1)
    draw.connect_p(node2,leaf2)

    return leaf1,leaf2

def F_graph_recur1(root,levels=1,scale=0,ax=None):

    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = F_graph1(root,scale,ax)
        if scale % 2 == 0:
            F_graph_recur2(leaf1,levels,scale+1,ax)
            F_graph_recur1(leaf2,levels,scale+1,ax)
        else:
            F_graph_recur1(leaf1,levels,scale+1,ax)
            F_graph_recur2(leaf2,levels,scale+1,ax)
        
def F_graph_recur2(root,levels=1,scale=0,ax=None):

    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = F_graph2(root,scale,ax)
        F_graph_recur1(leaf1,levels,scale+1,ax)
        F_graph_recur2(leaf2,levels,scale+1,ax)
        
def F_graph_example():
    draw.make_blank_canvas([-10,10],[-5,15],[14,14])
    F_graph_recur1([0,0],5)
    
    # Show the components
    draw.draw_rect_xy(-3,11.5,-1,14.5,ec='black',fc='white',zorder=-1)
    F_graph1([-2,12],3)
    draw.draw_rect_xy(1,11.5,3,14.5,ec='black',fc='white',zorder=-1)
    F_graph2([2,12],3)


    
if __name__ == '__main__':
    
    F_graph_example()
    draw.show_now()