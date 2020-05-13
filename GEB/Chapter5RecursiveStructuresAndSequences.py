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
    draw.connect_p(node1,leaf2)
    draw.connect_p(node1,node2)
    draw.connect_p(node2,leaf1)
    draw.draw_circle_p(node2,R=.1,ax=ax)
    
    return leaf1,leaf2

def G_graph_recur(root,levels=1,scale=0,ax=None):

    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = G_graph(root,scale,ax)
        G_graph_recur(leaf1,levels,scale+1,ax)
        G_graph_recur(leaf2,levels,scale+1,ax)


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
    draw.connect_p(node1,leaf2)
    draw.connect_p(node1,node2)
    draw.connect_p(node2,leaf1)
    draw.draw_circle_p(node2,R=.1,ax=ax)
    draw.draw_circle_p(node3,R=.1,ax=ax)
    
    return leaf1,leaf2

def H_graph_recur(root,levels=1,scale=0,ax=None):

    if scale >= levels:
        return 0
    else:
        leaf1,leaf2 = H_graph(root,scale,ax)
        H_graph_recur(leaf1,levels,scale+1,ax)
        H_graph_recur(leaf2,levels,scale+1,ax)
        H_graph_recur(leaf2,levels,scale+1,ax)


def F(n):
#    print(f"F({n})")
    if n == 0:
        return 1
    else:
        return n-M(F(n-1))
    
def M(n):
#    print(f"M({n})")
    if n == 0:
        return 0
    else:
        return n-F(M(n-1))


def Q(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Q(n-Q(n-1)) + Q(n-Q(n-2))


# RTN
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
    print(f"Ornate noun: {OrnateNoun()}")
    print(f"Fancy noun: {FancyNoun()}")
    
    print("\nG(n) = n-G(G(n-1))")
    for i in range(25):
        print(G(i),end=" ")

    draw.make_blank_canvas([-10,10],[-5,15],[8,8])
    G_graph_recur([0,0],5)
    draw.title("G(n) = n-G(G(n-1))",size=22)
    
    print("\nH(n) = n-H(H(H(n-1)))")
    for i in range(25):
        print(H(i),end=" ")

    draw.make_blank_canvas([-10,10],[-5,15],[8,8])
    H_graph_recur([0,0],5)
    draw.title("H(n) = n-H(H(H(n-1)))",size=22)

        
#    print("\n\nDiagram Q")
#    for i in range(1,25):
#        print(Q(i),end=" ")
        
    print("\nMarried Recursion")
    for i in range(25):
        print(M(i),end=" ")