from GEB.Chapter8TNT.Properties import is_var, get_vars, get_free_vars, is_num, \
                                       get_bound_vars, get_quants, is_term, is_atom, \
                                       is_compound
from GEB.Chapter8TNT.Translate import translate
from GEB.Chapter8TNT.StripSplit import split_eq, replace_var
from GEB.Chapter8TNT.Rules import *

# Need to create a hierarchical structure
class Deduction:
    
    def __init__(self,premise,depth=0,reality=None):
        self.theorems = [premise]
        self.theorems_description = ["premise"]
        self.depth = depth
        self.reality = reality
        
    def __str__(self):
        s = f"\n{' '*self.depth*2}["
        for num,(t,d) in enumerate(zip(self.theorems,self.theorems_description),1):
            if type(t) == Deduction:
                s += f"{' '*(self.depth*2+2)} {t}"
            else:
                s += f"\n{' '*(self.depth*2+2)}({num}) {t}"
        s += f"\n{' '*self.depth*2}]"
        return s
    
    # Force one-based indexing since this make more sense when counting steps
    def __getitem__(self,n):
        return self.theorems[n-1]
        
    def implication(self):
        if self.reality == None:
            return IMPLIES(self.theorems[1],self.theorems[-1])
        else:
            self.reality.theorems.append(IMPLIES(self.theorems[0],self.theorems[-1]))
    
    def fantasy(self,premise):
        d = Deduction(premise,self.depth+1,self)
        self.theorems.append(d)
        self.theorems_description.append("")
        return d
    
    def add_premise(self,premise):
        # At the lowest level we accept only axioms without justification
        # At all other levels we accept only known theorems
        if self.depth == 0:
            if premise not in ["∀a:~Sa=0","∀a:(a+0)=a",
                               "∀a:∀b:(a+Sb)=S(a+b)",
                               "∀a:(a⋅0)=0","∀a:∀b:(a⋅Sb)=((a⋅b)+a)"]:
                raise Exception(f"{premise} is not an axiom of TNT")                
        else:
            if premise not in self.reality.theorems:
                raise Exception(f"{premise} does not exist at the level one step lower")
        self.theorems.append(premise)
        self.theorems_description.append("premise")
        
    def specify(self,n,u,v):
        self.theorems.append(specify(self.theorems[n-1],u,v))
        self.theorems_description.append(f"specification of {n}")
        
    def symmetry(self,n):
        self.theorems.append(symmetry(self.theorems[n-1]))
        self.theorems_description.append(f"symmetry of {n}")
                
    def existence(self,n,u,v):
        self.theorems.append(existence(self.theorems[n-1],u,v))
        self.theorems_description.append(f"existence of {n}")
               
    def generalize(self,n,u):
        self.theorems.append(generalize(self.theorems[n-1],u))
        self.theorems_description.append(f"generalization of {n}")
                       
    def successor(self,n):
        self.theorems.append(successor(self.theorems[n-1]))
        self.theorems_description.append(f"successor of {n}")
                       
    def predecessor(self,n):
        self.theorems.append(predecessor(self.theorems[n-1]))
        self.theorems_description.append(f"predecessor of {n}")
               
    def transitivity(self,n1,n2):
        self.theorems.append(transitivity(self.theorems[n1-1],self.theorems[n2-1]))
        self.theorems_description.append(f"transitivity of {n1} and {n2}")
               
    def induction(self,t,u,n1,n2):
        self.theorems.append(induction(t,u,[self.theorems[n1-1],self.theorems[n2-1]]))
        self.theorems_description.append(f"induction on {n1} and {n2}")
    




if __name__ == '__main__':

    print("Build some statements of Typographical Number Theory")
    zero = "0"
    one = SUCC(zero)
    two = SUCC(one)
    b = "b"
    sq = MUL(b,b)
    sq_2 = EQ(sq,two)
    ex_sq_2 = EXISTS(sq_2,b)
    not_ex_sq_2 = NOT(ex_sq_2)
    print(zero)
    print(one)
    print(two)
    print(b)
    print(sq)
    print(sq_2)
    print(ex_sq_2)
    print(not_ex_sq_2)
    
    
    print("\n\n\nTranslation puzzles from GEB\n")
    for i in ["~∀c:∃b:(SS0⋅b)=c",
              "∀c:~∃b:(SS0⋅b)=c",
              "∀c:∃b:~(SS0⋅b)=c",
              "~∃b:∀c:(SS0⋅b)=c",
              "∃b:~∀c:(SS0⋅b)=c",
              "∃b:∀c:~(SS0⋅b)=c"]:
        print(f"{i}\n{translate(i)}\n")
    
    
    open_formula = "<∀b:d'-b∧~c=c>"
    print(f"\n\nVariables and quantifiers extracted from {open_formula}")
    print(f"Variables used {get_vars(open_formula)}")
    print(f"Quantifications used {get_quants(open_formula)}")
    print(f"Bound variables {get_bound_vars(open_formula)}")
    print(f"Free variables {get_free_vars(open_formula)}")
    

    terms = ["0","b","SSa'","(S0⋅(SS0+c))","S(Sa⋅(Sb⋅Sc))"]
    atoms = ["S0=0","(SS0+SS0)=SSSS0","S(b+c)=(S(c⋅d)⋅e)"]
    compounds = ["<S0=0⊃∀c:~∃b:(b+b)=c>"]

    parts_list = [terms,atoms,compounds]
    check_list = [is_term,is_atom,is_compound]
    name_list = ["Terms","Atoms","Compound Formulas"]
    
    print("\n\n\nChecking well-formedness\nAll should be well-formed (but may be false)")
    for parts,check,name in zip(parts_list,check_list,name_list):
        print(f"\n{name}")
        l = max([len(p) for p in parts])
        for p in parts:
            if check(p):
                print(f"{p:<{l}} {translate(p)}")
            else:
                print(f"{p:<{l}} ERROR")
    
    
    Pax1 = "∀a:~Sa=0"
    Pax2 = "∀a:(a+0)=a"
    Pax3 = "∀a:∀b:(a+Sb)=S(a+b)"
    Pax4 = "∀a:(a⋅0)=0"
    Pax5 = "∀a:∀b:(a⋅Sb)=((a⋅b)+a)"
    peano_axioms = [Pax1,Pax2,Pax3,Pax4,Pax5]
    print("\n\n\nAxioms of Peano Arithmetic")
    for i in peano_axioms:
        print(f"{i}\n{translate(i)}\n")
    
    
    print("\n\nRule of Specification")
    print(f"{Pax3} ⟹ {specify(Pax3,'a','(c+d)')}")
    print(f"{Pax4} ⟹ {specify(Pax4,'a','(S0⋅0)')}")
    print(f"{Pax5} ⟹ {specify(Pax5,'b','(S0+b)')}")
    print(f"")
    
    
    print("\n\n\nRules of Successorship")
    succ_example = "SSS0=S(S0+S0)"
    print(f"{succ_example} ⟹ {successor(succ_example)}")
    print(f"{succ_example} ⟹ {predecessor(succ_example)}")
    
    
    print("\n\n\nRule of Generalization")
    gen_example = "~S(c+SS0)=0"
    print(f"{gen_example} ⟹ {generalize(gen_example,'c')}")

    
    print("\n\n\nRule of Existence")
    print(f"{Pax1} ⟹ {existence(Pax1,'0','b')}")
    print(f"{Pax3} ⟹ {existence(Pax3,'Sb','c')}")
    
    
    print("\n\n\nRule of Transitivity")
    trans_example1 = "(a+b)=(a+S0)"
    trans_example2 = "(a+S0)=S(a+0)"
    print(f"{trans_example1}")
    print(f"{trans_example2}")
    print(f"{transitivity(trans_example1,trans_example2)}")


    print("\n\n\nDeduction Example from GEB")
    T = Deduction(Pax3)
    T.specify(1,'a','d')
    T.specify(2,'b','Sc')
    T.specify(1,'a','Sd')
    T.specify(4,'b','c')
    T.symmetry(5)
    
    F = T.fantasy("∀d:(d+Sc)=(Sd+c)")
    F.specify(1,'d','d')
    F.successor(2)
    F.add_premise(T[3])
    F.transitivity(4,3)
    F.add_premise(T[6])
    F.transitivity(5,6)
    F.generalize(7,'d')
    F.implication()
    
    T.generalize(8,'c')
    T.specify(2,'b','0')
    T.add_premise(Pax2)
    T.specify(11,'a','d')
    T.successor(12)
    T.transitivity(10,13)
    T.specify(11,'a','Sd')
    T.symmetry(15)
    T.transitivity(14,16)
    T.generalize(17,'d')
    T.induction("∀d:(d+Sc)=(Sd+c)",'c',9,18)
    T.specify(1,'a','c')
    T.specify(20,'b','d')
    T.specify(1,'a','d')
    T.specify(22,'b','c')
    T.symmetry(23)
    T.specify(19,'c','c')
    T.specify(25,'d','d')
    
    G = T.fantasy("∀c:(c+d)=(d+c)")
    G.specify(1,'c','c')
    G.successor(2)
    G.add_premise(T[21])
    G.transitivity(4,3)
    G.add_premise(T[24])
    G.transitivity(5,6)
    G.add_premise(T[26])
    G.transitivity(7,8)
    G.generalize(9,'c')
    G.implication()
    
    T.generalize(28,'d')
    T.specify(11,'a','c')
    T.specify(1,'a','0')
    T.specify(31,'b','b')
    
    H = T.fantasy("(0+b)=b")
    H.successor(1)
    H.add_premise(T[32])
    H.transitivity(3,2)
    H.implication()
    
    T.generalize(34,'b')
    T.specify(11,'a','0')
    T.induction("(0+b)=b",'b',35,36)
    T.specify(37,'b','c')
    T.symmetry(38)
    T.transitivity(30,39)
    T.generalize(40,'c')
    T.induction("∀c:(c+d)=(d+c)",'d',29,41)
    
    print(T)
    
    