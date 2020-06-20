from GEB.Chapter8TNT.Properties import is_var, get_vars, get_free_vars, is_num, \
                                       get_bound_vars, get_quants, is_term, is_atom, \
                                       is_compound, is_well_formed
from GEB.Chapter8TNT.Translate import translate, translate_arithmetic
from GEB.Chapter8TNT.StripSplit import split_eq, replace_var
from GEB.Chapter8TNT.Rules import *

PeanoAxioms = ["∀a:~Sa=0","∀a:(a+0)=a",
               "∀a:∀b:(a+Sb)=S(a+b)",
               "∀a:(a⋅0)=0","∀a:∀b:(a⋅Sb)=((a⋅b)+a)"]
AusterePeanoAxioms = ["∀a:~Sa=0","∀a:(a+0)=a",
                      "∀a:∀a':(a+Sa')=S(a+a')",
                      "∀a:(a⋅0)=0","∀a:∀a':(a⋅Sa')=((a⋅a')+a)"]

# Need to create a hierarchical structure
class Deduction:
    
    def __init__(self,premise,depth=0,reality=None):
        """
        Force deduction from reality to start with an axiom
        Otherwise any premise is allowed
        """
        self.theorems = [premise]
        if depth == 0:
            if premise not in PeanoAxioms:
                raise Exception("Must begin with an axiom of TNT")
                
        if premise in PeanoAxioms:
            self.descriptions = [f"axiom"]
        else:
            self.descriptions = [f"premise"]
        
        self.depth = depth
        self.reality = reality
        
    def write_theorems(self):
        """
        Write out the deduction with lines numbered from 1
        Fantasies are indented relative to their depth
        The fantasy will count its own steps and the reality below it only 
        counts one step in the form of implication
        """
        s = f"\n{' '*self.depth*2}["
        for line,t in enumerate(self.theorems,1):
            line_number = f"({line})"
            if type(t) == Deduction:
                s += f"{t.write_theorems()}"
            else:
                s += f"\n{' '*(self.depth*2+2)}{line_number:>4} {t}"
        s += f"\n{' '*self.depth*2}]"
        return s
    
    def write_descriptions(self):
        """
        Write out the descriptions of each line
        """
        s = f"\n{' '*self.depth*2}["
        for line,(d,t) in enumerate(zip(self.descriptions,self.theorems),1):
            line_number = f"({line})"
            if type(t) == Deduction:
                s += f"{t.write_descriptions()}"
            else:
                s += f"\n{' '*(self.depth*2+2)}{line_number:>4} {d}"
        s += f"\n{' '*self.depth*2}]"
        return s
    
    def write_theorems_and_descriptions(self):
        """
        Write out the theorems and their descriptions together
        """
        max_length = 0
        for t in self.theorems:
            if type(t) == Deduction:
                continue
            max_length = max(max_length,len(t))
            
        s = f"\n{' '*self.depth*2}["
        for line,(d,t) in enumerate(zip(self.descriptions,self.theorems),1):
            
            line_number = f"({line})"
            
            if type(t) == Deduction:
                s += f"{t.write_theorems_and_descriptions()}"
            else:
                s += f"\n{' '*(self.depth*2+2)}{line_number:<4} {t:<{max_length}} {d}"
        s += f"\n{' '*self.depth*2}]"
        return s
    
    # Force one-based indexing since this make more sense when counting steps
    def __getitem__(self,n):
        return self.theorems[n-1]
    
    def implication(self):
        """Implication of a fantasy"""
        if self.reality == None:
            raise Exception("Implication rule only applies within a fantasy")
        else:
            self.reality.theorems.append(IMPLIES(self.theorems[0],self.theorems[-1]))
            self.reality.descriptions.append(f"implication")

    def fantasy(self,premise):
        """Begin deduction on an arbitrary premise"""
        d = Deduction(premise,self.depth+1,self)
        self.theorems.append(d)
        self.descriptions.append(f"fantasy")
        return d

    def add_premise(self,premise):
        """
        At the lowest level we accept only axioms without justification
        At all other levels we accept only known theorems
        """
        if self.depth == 0:
            if premise not in PeanoAxioms:
                raise Exception(f"{premise} is not an axiom of TNT")                
        else:
            if premise not in self.reality.theorems:
                raise Exception(f"{premise} does not exist at the level one step lower")
        self.theorems.append(premise)
        if premise in PeanoAxioms:
            self.descriptions.append(f"axiom")
        else:
            self.descriptions.append(f"premise")

    def specify(self,n,u,v):
        T = specify(self.theorems[n-1],u,v)
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"specification of {n}")
        else:
            raise Exception(f"{T} is not well-formed")

    def symmetry(self,n):
        T = symmetry(self.theorems[n-1])
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"symmetry of {n}")
        else:
            raise Exception(f"{T} is not well-formed")

    def existence(self,n,u,v):
        T = existence(self.theorems[n-1],u,v)
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"existence of {n}")
        else:
            raise Exception(f"{T} is not well-formed")

    def generalize(self,n,u):
        T = generalize(self.theorems[n-1],u)
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"generalization of {n}")
        else:
            raise Exception(f"{T} is not well-formed")

    def successor(self,n):
        T = successor(self.theorems[n-1])
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"successor of {n}")
        else:
            raise Exception(f"{T} is not well-formed")

    def predecessor(self,n):
        T = predecessor(self.theorems[n-1])
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"(predecessor of {n}")
        else:
            raise Exception(f"{T} is not well-formed")

    def transitivity(self,n1,n2):
        T = transitivity(self.theorems[n1-1],self.theorems[n2-1])
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"transitivity of {n1} and {n2}")
        else:
            raise Exception(f"{T} is not well-formed")      

    def induction(self,t,u,n1,n2):
        T = induction(t,u,[self.theorems[n1-1],self.theorems[n2-1]])
        if is_well_formed(T):
            self.theorems.append(T)
            self.descriptions.append(f"induction on {n1} and {n2}")
        else:
            raise Exception(f"{T} is not well-formed") 





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
    

    print("\n\n\nTranslated Axioms of Peano Arithmetic")
    for i in PeanoAxioms:
        print(f"{i}\n{translate(i)}\n")
   
    print("\n\nArithmetized Axioms of Peano Arithmetic")
    for i in AusterePeanoAxioms:
        print(f"{i}\n{translate_arithmetic(i)}\n")
    
    
    print("\n\nRule of Specification")
    print(f"{PeanoAxioms[1]} ⟹ {specify(PeanoAxioms[1],'a','(c+d)')}")
    print(f"{PeanoAxioms[3]} ⟹ {specify(PeanoAxioms[3],'a','(S0⋅0)')}")
    print(f"{PeanoAxioms[4]} ⟹ {specify(PeanoAxioms[4],'b','(S0+b)')}")
    
    
    print("\n\n\nRules of Successorship")
    succ_example = "SSS0=S(S0+S0)"
    print(f"{succ_example} ⟹ {successor(succ_example)}")
    print(f"{succ_example} ⟹ {predecessor(succ_example)}")
    
    
    print("\n\n\nRule of Generalization")
    gen_example = "~S(c+SS0)=0"
    print(f"{gen_example} ⟹ {generalize(gen_example,'c')}")

    
    print("\n\n\nRule of Existence")
    print(f"{PeanoAxioms[0]} ⟹ {existence(PeanoAxioms[0],'0','b')}")
    print(f"{PeanoAxioms[2]} ⟹ {existence(PeanoAxioms[2],'Sb','c')}")
    
    
    print("\n\n\nRule of Transitivity")
    trans_example1 = "(a+b)=(a+S0)"
    trans_example2 = "(a+S0)=S(a+0)"
    print(f"{trans_example1}")
    print(f"{trans_example2}")
    print(f"{transitivity(trans_example1,trans_example2)}")


#    print("\n\n\nDeduction of Commutativity")
#    T = Deduction(PeanoAxioms[2])
#    T.specify(1,'a','d')
#    T.specify(2,'b','Sc')
#    T.specify(1,'a','Sd')
#    T.specify(4,'b','c')
#    T.symmetry(5)
#    
#    F = T.fantasy("∀d:(d+Sc)=(Sd+c)")
#    F.specify(1,'d','d')
#    F.successor(2)
#    F.add_premise(T[3])
#    F.transitivity(4,3)
#    F.add_premise(T[6])
#    F.transitivity(5,6)
#    F.generalize(7,'d')
#    F.implication()
#    
#    T.generalize(8,'c')
#    T.specify(2,'b','0')
#    T.add_premise(PeanoAxioms[1])
#    T.specify(11,'a','d')
#    T.successor(12)
#    T.transitivity(10,13)
#    T.specify(11,'a','Sd')
#    T.symmetry(15)
#    T.transitivity(14,16)
#    T.generalize(17,'d')
#    T.induction("∀d:(d+Sc)=(Sd+c)",'c',9,18)
#    T.specify(1,'a','c')
#    T.specify(20,'b','d')
#    T.specify(1,'a','d')
#    T.specify(22,'b','c')
#    T.symmetry(23)
#    T.specify(19,'c','c')
#    T.specify(25,'d','d')
#    
#    G = T.fantasy("∀c:(c+d)=(d+c)")
#    G.specify(1,'c','c')
#    G.successor(2)
#    G.add_premise(T[21])
#    G.transitivity(4,3)
#    G.add_premise(T[24])
#    G.transitivity(5,6)
#    G.add_premise(T[26])
#    G.transitivity(7,8)
#    G.generalize(9,'c')
#    G.implication()
#    
#    T.generalize(28,'d')
#    T.specify(11,'a','c')
#    T.specify(1,'a','0')
#    T.specify(31,'b','b')
#    
#    H = T.fantasy("(0+b)=b")
#    H.successor(1)
#    H.add_premise(T[32])
#    H.transitivity(3,2)
#    H.implication()
#    
#    T.generalize(34,'b')
#    T.specify(11,'a','0')
#    T.induction("(0+b)=b",'b',35,36)
#    T.specify(37,'b','c')
#    T.symmetry(38)
#    T.transitivity(30,39)
#    T.generalize(40,'c')
#    T.induction("∀c:(c+d)=(d+c)",'d',29,41)
#    
#    print(T.write_theorems_and_descriptions())