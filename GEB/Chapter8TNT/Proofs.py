from GEB.Chapter8TNT.Chapter8TNT import Deduction, PeanoAxioms
from GEB.Chapter8TNT.Translate import translate

for n,i in enumerate(PeanoAxioms):
    print(n,i)


print("\n\nProve 0 is a Natural Number")
A = Deduction(PeanoAxioms[1])
A.specify(1,'a','0')
A.existence(2,'(0+0)','a')
print(A.theorems_and_descriptions)
print(translate(A[3]))


print("\n\nProve 0=0")
B = Deduction(PeanoAxioms[1])
B.specify(1,'a','0')
B.symmetry(2)
B.transitivity(3,2)
print(B.theorems_and_descriptions)
print(translate(B[4]))


print("\n\nProve 1+1=2")
C = Deduction(PeanoAxioms[2])
C.specify(1,'a','S0')
C.specify(2,'b','0')
C.add_axiom(PeanoAxioms[1])
C.specify(4,'a','S0')
C.successor(5)
C.transitivity(3,6)
print(C.theorems_and_descriptions)
print(translate(C[7]))


print("\n\nProve Every Natural Number has a Successor")
D = Deduction(PeanoAxioms[1])
D.specify(1,'a','a')
D.successor(2)
D.existence(3,'S(a+0)','b')
D.generalize(4,'a')
print(D.theorems_and_descriptions)
print(translate(D[5]))


#print("\n\nProve 5 is Prime")
#E = Deduction(PeanoAxioms[0])
#E.interchange_EA(1,'a',0)
#print(E.theorems_and_descriptions)