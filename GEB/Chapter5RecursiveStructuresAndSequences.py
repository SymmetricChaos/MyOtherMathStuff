import numpy as np
def G(n):
    if n == 0:
        return 0
    else:
        return n-G(G(n-1))


def H(n):
    if n == 0:
        return 0
    else:
        return n-H(H(H(n-1)))


def F(n):
    if n == 0:
        return 1
    else:
        return n-F(M(n-1))
    
def M(n):
    if n == 0:
        return 0
    else:
        return n-M(F(n-1))


def Q(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Q(n-Q(n-1)) + Q(n-Q(n-2))


# RTN
adj_list = ["acidic","basic","small","large","hot","cold","bright","dark","red","green","blue","orange","tall","short","clean","dirty"]
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
    
    #Recreate the graphs from the book
    
    print("\nDiagram G")
    for i in range(25):
        print(G(i),end=" ")
    
    print("\n\nDiagram H")
    for i in range(25):
        print(H(i),end=" ")
        
    print("\n\nDiagram Q")
    for i in range(1,25):
        print(Q(i),end=" ")
        
#    print("\nMarried Recursion")
#    for i in range(10):
#        print(M(i),end=" ")