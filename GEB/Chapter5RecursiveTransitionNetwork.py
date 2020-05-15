import numpy as np


# Simple Fibonnaci number generator
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# Just for fun a function that expands a particular input to show all the
# recusion done.
def fib_expansion_recur(n):
    if n == 0:
        return "1"
    if n == 1:
        return "1"
    else:
        return f"fib({fib_expansion_recur(n-1)}) + fib({fib_expansion_recur(n-2)})"
    
def fib_expansion(n):
    
    return f"fib({n}) = {fib_expansion_recur(n)}"





# Recursive Transition Network
adj_list = ["acidic","basic","small","large","hot","cold","bright","dark","red","green","blue","orange","tall","short","clean","dirty","simple","complex"]
noun_list = ["animal","plant","rock","computer","book","desk","fan","bottle","person","oven","country","thing","child","adult","road"]
prep_list = ["about","above","across","after","against","among","around","at","before","behind","below","beside","between","by","down","during","except","for","from","in","inside","into","near","of","off","on","out","over","through","to","toward","under","up","with"]
verb_list = ["chose","wore","bought","flew","dropped","grabbed","ate","climbed","threw","jumped"]
rel_pronoun_list = ["who","which","that"]

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
    
    print("Expansions of the Fibonacci reccurence")
    for i in range(6):
        print(fib_expansion(i))
        
    # Ornate Noun
    print("\n\nCreate a complex noun phrase using a recursive formula\nNote that a grammatical noun phrase is more sophisticated than this and must respect things like adjective order and correct articles.")
    print(f"Fancy noun: {FancyNoun()}")
    print(f"Fancy noun: {FancyNoun()}")
    