from GEB.Chapter8TNT.Properties import is_var, get_vars, get_free_vars, is_num, \
                                       get_bound_vars, get_quants, is_term, is_atom, \
                                       is_compound
from GEB.Chapter8TNT.Translate import translate
from GEB.Chapter8TNT.StripSplit import split_eq, replace_var
from GEB.Chapter8TNT.Rules import *

# Need to create a hierarchical structure
class Deduction:
    
    def __init__(self,premise,depth=0):
        self.theorems = [premise]
        self.depth = depth
        
    def __str__(self):
        s = f"\n{' '*self.depth*2}["
        for num,t in enumerate(self.theorems):
            s += f"\n{' '*(self.depth*2+1)}({num}) {t}"
        s += f"\n{' '*self.depth*2}]"
        return s
    
    def __getitem__(self,n):
        return self.theorems[n]
        
    def implication(self):
        return IMPLIES(self.theorems[0],self.theorems[-1])
    
    def fantasy(self,premise):
        d = Deduction(premise,self.depth+1)
        self.theorems.append(d)
        return d
    
    def add_premise(self,premise):
        self.theorems.append(premise)
        
    def specify(self,n,u,v):
        self.theorems.append(specify(self.theorems[n],u,v))
        
    def symmetry(self,n):
        self.theorems.append(symmetry(self.theorems[n]))
        
    def existence(self,n,u,v):
        self.theorems.append(existence(self.theorems[n],u,v))
        
    def generalize(self,n,u):
        self.theorems.append(generalize(self.theorems[n],u))
        
    def successor(self,n):
        self.theorems.append(successor(self.theorems[n]))
        
    def predecessor(self,n):
        self.theorems.append(predecessor(self.theorems[n]))

    def transitivity(self,n1,n2):
        self.theorems.append(transitivity(self.theorems[n1],self.theorems[n2]))



    




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


    print("\n\n\nFantasy")
    T = Deduction(Pax3)
    T.specify(0,'a','d')
    T.specify(1,'b','Sc')
    T.specify(0,'a','Sd')
    T.specify(3,'b','c')
    T.symmetry(4)
    F = T.fantasy("∀d:(d+Sc)=(Sd+c)")
    F.specify(0,'d','d')
    F.successor(1)
    F.add_premise(T[2])
    F.transitivity(3,2)
    F.add_premise(T[5])
    F.transitivity(4,5)
    F.generalize(6,'d')
    T.add_premise(F.implication())
    print(T)
    
    