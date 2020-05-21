def pq_axioms():
    n = 0
    while True:
        p = "-"*n + "p-q" + "-"*n + "-"
        yield p
        n += 1
        
def pq_production(s):
    left, right = s.split("q")
    return left + "-q" + right + "-"

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
            
        
    
    
# Recusrively check validity of a pq-statement
def well_formed_pq(S):
    pass
        
    





if __name__ == '__main__':

    print("Enumerating the theorems of the pq-system not only produces simple addition theorems but it lists them in order of increasing value")
    for enum,theorem in enumerate(pq_all_theorems()):
        print(theorem)
        if enum > 20:
            break