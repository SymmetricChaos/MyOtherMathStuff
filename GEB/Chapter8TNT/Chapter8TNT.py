from GEB.Chapter8TNT.Properties import get_vars, get_free_vars, \
                                       get_bound_vars, get_quants
from GEB.Chapter8TNT.Translate import translate, translate_arithmetic
from GEB.Chapter8TNT.Rules import *
from GEB.Chapter8TNT.Deduction import Deduction, PeanoAxioms, AusterePeanoAxioms


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
    

    print("\n\n\nDeduction of Commutativity")
    T = Deduction(PeanoAxioms[2])
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
    T.add_premise(PeanoAxioms[1])
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
    
    print(T.theorems_and_descriptions)