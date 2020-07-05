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
print(translate(A[-1]))


print("\n")
B = Deduction("Prove 1+1=2")
B.add_premise(PeanoAxioms[2])
B.specify(1,'a','S0')
B.specify(2,'b','0')
B.add_premise(PeanoAxioms[1])
B.specify(4,'a','S0')
B.successor(5)
B.transitivity(3,6)
print(B.theorems_and_descriptions)
print(translate(B[-1]))


print("\n")
C = Deduction("Prove Every Natural Number has a Successor")
C.add_premise(PeanoAxioms[1])
C.specify(1,'a','a')
C.successor(2)
C.existence(3,'S(a+0)','b')
C.generalize(4,'a')
print(C.theorems_and_descriptions)
print(translate(C[-1]))


print("\n")
D = Deduction("Prove 1 is the (Left) Multiplicative Identity")
D.add_premise(PeanoAxioms[3])
D.specify(1,"a","S0"," [the base case]")
d1 = D.fantasy("∀a:(S0⋅a)=a")
d1.specify(1,"a","Sa")
d1.implication()
D.specify(4,"a","a")
D.generalize(5,"a"," [the general case]")
D.induction("(S0⋅a)=a","a",2,6)
print(D.theorems_and_descriptions)
print(translate(D[-1]))

