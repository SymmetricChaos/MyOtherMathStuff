import numpy as np
import Utils.Drawing as draw

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





# Recursive Transition Network
adj_list = ["acidic","basic","small","large","hot","cold","bright","dark","red","green","blue","orange","tall","short","clean","dirty","simple","complex"]
noun_list = ["animal","plant","rock","computer","book","desk","fan","bottle","person","oven","country","thing","child","adult","road"]
prep_list = ["about","above","across","after","against","among","around","at","before","behind","below","beside","between","by","down","during","except","for","from","in","inside","into","near","of","off","on","out","over","through","to","toward","under","up","with"]
verb_list = ["chose","wore","bought","flew","dropped","grabbed","ate","climbed","threw","jumped"]
rel_pronoun_list = ["who","which","that","whom"]

def Article():
    return np.random.choice(["a","an","the"],1)[0]

def Adjective():
    return np.random.choice(adj_list,1)[0]

def Noun():
    return np.random.choice(noun_list,1)[0]

def Preposition():
    return np.random.choice(prep_list,1)[0]

def Verb():
    return np.random.choice(verb_list,1)[0]

def RelativePronoun():
    return np.random.choice(rel_pronoun_list,1)[0]

def OrnateNoun():
    S = ""
    S += Article() + " "
    while np.random.uniform() > .5:
        S += Adjective() + " "
    S += Noun()
    return S
    
def FancyNoun():
    S = ""
    path = np.random.randint(0,2)
    
    if path == 0:
        S += OrnateNoun() + " "
        S += Preposition() + " "
        S += FancyNoun()
    
    elif path == 1:
        S += OrnateNoun() + " "
        S += RelativePronoun() + " "
        S += Verb() + " "
        S += OrnateNoun()
    
    elif path == 2:
        S += OrnateNoun() + " "
        S += RelativePronoun() + " "
        S += OrnateNoun() + " "
        S += Verb()
        
    return S

    



if __name__ == '__main__':

    # Ornate Noun
    print(f"Fancy noun: {FancyNoun()}")
    print(f"Fancy noun: {FancyNoun()}")
    
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
    

    print("\n\nDiagram Q")
    print("n   :",end=" ")
    for i in range(1,25):
        print(f"{i:>2}",end=" ")
    print("\nQ(n):",end=" ")
    for i in range(1,25):
        print(f"{Q(i):>2}",end=" ")
