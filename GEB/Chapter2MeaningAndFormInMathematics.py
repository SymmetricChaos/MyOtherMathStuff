# The pq-system is a toy formal system that is an analogue for simple addition
# of the form x+y=z over the integers

def pq_axioms():
    n = 1
    while True:
        p = "-"*n + "p-q" + "-"*n + "-"
        yield p
        n += 1
        
def pq_axioms_alt():
    n = 1
    while True:
        p = "-p" + "-"*n + "q" + "-"*n + "-"
        yield p
        n +=  1
        
        
def pq_production(s):
    left, right = s.split("q")
    return left + "-q" + right + "-"

def pq_production_alt(s):
    left, right = s.split("p")
    return left + "-" + "p" + right + "-"


def pq_all_theorems():
    old_theorems = []
    new_theorems = []
    
    # At each stage we yield a new axiom
    for new_ax in pq_axioms():
        yield new_ax
        old_theorems.append(new_ax)
        
        # New we go through the list of theorems to consider and produce a new
        # theorem from each of them
        # Note that we don't need keep a list of ALL previous theorems just the
        # ones produced last time
        
        for theorem in old_theorems:
            nt = pq_production(theorem)
            new_theorems.append(nt)
            yield nt
            
        old_theorems = new_theorems.copy()
        new_theorems = []


# Crudest possible check check for being well-formed
def well_formed_pq(S):
    for t in pq_all_theorems():
        if t == S:
            return True
        if len(t) > len(S):
            return False





if __name__ == '__main__':

    print("Enumerating the theorems of the pq-system not only produces simple addition theorems but it lists them in order of increasing value")
    for enum,theorem in enumerate(pq_all_theorems()):
        print(theorem)
        if enum > 19:
            break
    
    print("\n\nIn a formal system all statements are formally correct or formally incorrect. However the reason for the interpretation being true or false may vary. The final example below is formally incorrect but would interpret as a true statement. In that case it is because the pq-system does not define an analogue to zero.")
    strings = ["--p--p----",
               "---p--q-----",
               "-p-q---",
               "-pq-"]
    for s in strings:
        if well_formed_pq(s):
            print(f"{s:<12} is well formed")
        else:
            print(f"{s:<12} is not well formed")