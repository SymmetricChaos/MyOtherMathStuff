from GEB.Chapter8TNT.Deduction import Deduction, PeanoAxioms
from GEB.Chapter8TNT.Translate import translate

for n,i in enumerate(PeanoAxioms):
    print(n,i)

print("\n")
A = Deduction("Prove 0 is a Natural Number")
A.add_premise(PeanoAxioms[1])
A.specify(1,'a','0')
A.existence(2,'(0+0)','a')
print(A.theorems_and_descriptions)
print(translate(A[3]))


print("\n")
B = Deduction("Prove 0=0")
B.add_premise(PeanoAxioms[1])
B.specify(1,'a','0')
B.symmetry(2)
B.transitivity(3,2)
print(B.theorems_and_descriptions)
print(translate(B[4]))


print("\n")
C = Deduction("Prove 1+1=2")
C.add_premise(PeanoAxioms[2])
C.specify(1,'a','S0')
C.specify(2,'b','0')
C.add_premise(PeanoAxioms[1])
C.specify(4,'a','S0')
C.successor(5)
C.transitivity(3,6)
print(C.theorems_and_descriptions)
print(translate(C[7]))


print("\n")
D = Deduction("Prove Every Natural Number has a Successor")
D.add_premise(PeanoAxioms[1])
D.specify(1,'a','a')
D.successor(2)
D.existence(3,'S(a+0)','b')
D.generalize(4,'a')
print(D.theorems_and_descriptions)
print(translate(D[5]))


print("\n")
E = Deduction("Prove 1 is the (Left) Multiplicative Identity")
E.add_premise(PeanoAxioms[3])
E.specify(1,"a","S0"," [the base case]")
e1 = E.fantasy("∀a:(S0⋅a)=a")
e1.specify(1,"a","Sa")
e1.implication()
E.specify(4,"a","a")
E.generalize(5,"a"," [the general case]")
E.induction("(S0⋅a)=a","a",2,6)
print(E.theorems_and_descriptions)
print(translate(E[7]))
