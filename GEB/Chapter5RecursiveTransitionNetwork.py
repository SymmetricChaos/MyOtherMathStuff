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
noun_list = ["animal","plant","rock","computer","book","desk","fan","bottle","person","oven","country","thing","child","adult","road","family","river","ocean","woman","man","dragon","planet","snack","doctor","meat","library","button","paper"]
prep_list = ["about","above","across","after","against","among","around","before","behind","below","beside","between","by","from","in","inside","into","near","on","over","to","toward","under","with"]
verb_list = ["chose","wore","bought","flew","dropped","grabbed","ate","climbed","threw","jumped","attacked","helped","twirled","insulted","complimented"]
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

# Selects adjectives in a way that respect the typical adjective order in English
def ComplexAdjective():

    # Opinion
    opinion = ["beautiful","useless","horrible","amazing","excellent","skillful","strange","unusual","bizzare","ordinary"]
    # Size
    size = ["big","small","huge","tiny","tremendous","tall","short","long","diminutive","fat","thin","narrow"]
    # Physical quality
    quality = ["dirty","clean","rough","smooth","soft","hard","fragile"]
    # Age
    age = ["old","young","baby","ancient","geriatric","infantile","modern","classical"]
    # Shape
    shape = ["square","round","triangular","cubical","convex","concave","spherical","rectangular"]
    # Color
    color = ["red","orange","yellow","green","blue","indigo","violet","pink","brown","black","white","colorless","transparent"]
    # Title/Origin
    origin = ["American","French","Chinese","Russian","Egyptian","Australian","Turkish","Dutch","northern","southern","eastern","western"]
    # Material
    material = ["wooden","metal","plastic","ceramic","cotton"]

    A = ""
    
    # go through the lists in order randomly picking adjectives
    for adj_list in [opinion, size, quality, age, shape, color, origin, material]:
        # how much to reduce the chance of adding an adjective of the same kind
        rep_adjust = 0
        while np.random.uniform() < (.15-rep_adjust):
            A += np.random.choice(adj_list,1)[0] + " "
            rep_adjust += .03
    
    return A

def ChooseArticle(s):
    if s[0] in "aeiou":
        return np.random.choice(["an","the"],1)[0]
    else:
        return np.random.choice(["a","the"],1)[0]

def SimpleNounPhrase():
    noun = np.random.choice(noun_list,1)[0]
    c_adj = ComplexAdjective()
    
    phrase = c_adj + noun
    art = ChooseArticle(phrase)
    return art + " " + phrase

def ComplexNounPhrase():
    S = ""
    path = np.random.randint(0,2)
    
    if path == 0:
        S += SimpleNounPhrase() + " "
        S += Preposition() + " "
        S += ComplexNounPhrase()
    
    elif path == 1:
        S += SimpleNounPhrase() + " "
        S += RelativePronoun() + " "
        S += Verb() + " "
        S += SimpleNounPhrase()
    
    elif path == 2:
        S += SimpleNounPhrase() + " "
        S += RelativePronoun() + " "
        S += SimpleNounPhrase() + " "
        S += Verb()
        
    return S
    
    
    
    
    

if __name__ == '__main__':
    
    print("Expansions of the Fibonacci reccurence")
    for i in range(6):
        print(fib_expansion(i))
        
    # Ornate Noun
    print("\n\nCreate a complex noun phrase using a recursive formula\nNote that a grammatical noun phrase is more sophisticated than this and must respect things like adjective order and correct articles.\n")
    print(f"Fancy noun: {FancyNoun()}")
    print(f"Fancy noun: {FancyNoun()}")
    
    
    # A more sophisticated grammatical system
    print("\n\nA slightly more complicated system that better respects how English is spoken. Note that this system still often produces nonsense because it cannot consider context.\n")
    print(f"Plain Noun: {Noun()}")
    print(f"Simple Noun: {SimpleNounPhrase()}")
    print(f"Complex Noun: {ComplexNounPhrase()}")