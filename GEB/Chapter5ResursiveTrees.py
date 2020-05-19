import Utils.Drawing as draw
import numpy as np


def G(n):
    if n == 0:
        return 0
    else:
        return n-G(G(n-1))
    
def G_graph(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]+5*s , root[1]+1 ]
    leaf1 = [ root[0]+5*s , root[1]+2 ]
    leaf2 = [ root[0]-5*s , root[1]+1 ]
    
    draw.draw_circle_p(node1,R=.1,ax=ax)
    draw.draw_circle_p(node2,R=.1,ax=ax)
    draw.connect_p(node1,leaf2)
    draw.connect_p(node1,node2)
    draw.connect_p(node2,leaf1)

    return leaf1,leaf2

def G_graph_recur(root,levels=1,scale=0,ax=None):

    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = G_graph(root,scale,ax)
        G_graph_recur(leaf1,levels,scale+1,ax)
        G_graph_recur(leaf2,levels,scale+1,ax)

def G_graph_example():
    draw.make_blank_canvas([-10,10],[-5,15],[14,14])
    G_graph_recur([0,0],5)
    draw.title("G(n) = n-G(G(n-1))",size=22)
    draw.draw_rect_xy(1,11.5,3,14.5,ec='black',fc='white',zorder=-1)
    G_graph([2,12],3)





def H(n):
    if n == 0:
        return 0
    else:
        return n-H(H(H(n-1)))

def H_graph(root,scale=0,ax=None):
    s = 1/(2**scale)
    node1 = root
    node2 = [ root[0]+5*s , root[1]+1 ]
    node3 = [ root[0]+5*s , root[1]+2 ]
    leaf1 = [ root[0]+5*s , root[1]+3 ]
    leaf2 = [ root[0]-5*s , root[1]+1 ]
    
    draw.draw_circle_p(node1,R=.1,ax=ax)
    draw.draw_circle_p(node2,R=.1,ax=ax)
    draw.draw_circle_p(node3,R=.1,ax=ax)
    draw.connect_p(node1,leaf2)
    draw.connect_p(node1,node2)
    draw.connect_p(node2,leaf1)

    return leaf1,leaf2

def H_graph_recur(root,levels=1,scale=0,ax=None):

    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = H_graph(root,scale,ax)
        H_graph_recur(leaf1,levels,scale+1,ax)
        H_graph_recur(leaf2,levels,scale+1,ax)
        
def H_graph_example():
    draw.make_blank_canvas([-10,10],[-5,15],[14,14])
    H_graph_recur([0,-3],5)
    draw.title("H(n) = n-H(H(H(n-1)))",size=22)
    draw.draw_rect_xy(1,10.5,3,14.5,ec='black',fc='white',zorder=-1)
    H_graph([2,11],3)





# Married recursion
def F(n):
    if n == 0:
        return 1
    else:
        return n-M(F(n-1))
    
def M(n):
    if n == 0:
        return 0
    else:
        return n-F(M(n-1))
    
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
    draw.draw_rect_xy(-3,11.5,-1,14.5,ec='black',fc='white',zorder=-1)
    F_graph1([-2,12],3)
    draw.draw_rect_xy(1,11.5,3,14.5,ec='black',fc='white',zorder=-1)
    F_graph2([2,12],3)
    draw.title("F(n) = n-M(F(n-1))), F(0) = 1\nM(n) = n-F(M(n-1))), M(0) = 0",size=22)






def Q(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Q(n-Q(n-1)) + Q(n-Q(n-2))





# A version of INT from the book
def INT(x):
    
    if x < .5:
        for denom in [2,4,8,16,32,64,128,256,512,1024]:
            if x <= 1/denom:
                continue
            else:
                return x+((denom-3)/denom)
            
    if x >= .5:
        for denom in [2,4,8,16,32,64,128,256,512,1024]:
            if x >= (denom-1)/denom:
                continue
            else:
                return x-((denom-3)/denom)

    return 1-x

def INT_range(x,lo,hi):
    if lo < .5:
        x = (x-lo)/(hi-lo)
        x = INT(x)
        return (x*(hi-lo))+lo
    if lo >= .5:
        x = (x-lo)/(hi-lo)
        x = INT(x)
        return (x*(hi-lo))+lo


def INT_level_2():
    for denom in [4,8,16,32,64,128,256,512,1024]:
        lo = 1/denom*2
        hi = 1/denom
        x1 = np.linspace(lo,hi,100)
        y1 = [1-INT_range(i,lo,hi) for i in x1]
        draw.draw_dots_xy(x1,y1,s=.5,color='black')
        
    for denom in [2,4,8,16,32,64,128,256,512,1024]:
        lo = (denom-1)/denom
        hi = (denom*2-1)/(denom*2)
        x1 = np.linspace(lo,hi,100)
        y1 = [1-INT_range(i,lo,hi) for i in x1]
        draw.draw_dots_xy(x1,y1,s=.5,color='black')





if __name__ == '__main__':

    print("\n\n\nG(n) = n-G(G(n-1)), G(0) = 0")
    print("n   :",end=" ")
    for i in range(25):
        print(f"{i:>2}",end=" ")
    print("\nG(n):",end=" ")
    for i in range(25):
        print(f"{G(i):>2}",end=" ")
    G_graph_example()
    draw.show_now()
    
    
    print("\n\n\nH(n) = n-H(H(H(n-1))), H(0) = 0")
    print("n   :",end=" ")
    for i in range(25):
        print(f"{i:>2}",end=" ")
    print("\nH(n):",end=" ")
    for i in range(25):
        print(f"{H(i):>2}",end=" ")
    H_graph_example()
    draw.show_now()
    
    
    print("\n\n\nF(n) = n-M(F(n-1)), F(0) = 1\nM(n) = n-F(M(n-1)), M(0) = 0")
    print("n   :",end=" ")
    for i in range(25):
        print(f"{i:>2}",end=" ")
    print("\nF(n):",end=" ")
    for i in range(25):
        print(f"{F(i):>2}",end=" ")
    print("\nM(n):",end=" ")
    for i in range(25):
        print(f"{M(i):>2}",end=" ")
    F_graph_example()
    draw.show_now()
 
    
    print("\n\n\nWhile the recusive functions above have regular structure shown by the trees the function below apparently does not.")
    print("Q(n) = Q(n-Q(n-1)) + Q(n-Q(n-2)), Q(1) = Q(2) = 1")
    print("n   :",end=" ")
    for i in range(1,25):
        print(f"{i:>2}",end=" ")
    print("\nQ(n):",end=" ")
    for i in range(1,25):
        print(f"{Q(i):>2}",end=" ")
        
    print("\n\n\n")
    draw.make_blank_canvas([0,1],[0,1],[16,16])
    INT_level_2()
    draw.title("Adapatation of INT from GEB\nNote that this isn't a function on x since there are slight overlaps\nProbably while Hofstader's function bends",size=22)