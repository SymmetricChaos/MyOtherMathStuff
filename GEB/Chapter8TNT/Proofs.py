from GEB.Chapter8TNT.Chapter8TNT import Deduction, PeanoAxioms

for n,i in enumerate(PeanoAxioms):
    print(n,i)




print("\n\nProve 0=0")
A = Deduction(PeanoAxioms[1])
A.specify(1,'a','0')
A.symmetry(2)
A.transitivity(3,2)
print(A.write_theorems_and_descriptions())



print("\n\nProve 1+1=2")
B = Deduction(PeanoAxioms[2])
B.specify(1,'a','S0')
B.specify(2,'b','0')
B.add_axiom(PeanoAxioms[1])
B.specify(4,'a','S0')
B.successor(5)
B.transitivity(3,6)
print(B.write_theorems_and_descriptions())



#print("\n\nProve 2⋅2=4")
#C = Deduction(PeanoAxioms[4])
#C.specify(1,'a','SS0')
#C.specify(2,'b','S0')
#C.add_axiom(PeanoAxioms[1])
#C.specify(4,'a','SSSS0')
#
#print(C.write_theorems_and_descriptions())


print("\n\nProve 0 is a Natural Number ∃a:a=0")
D = Deduction(PeanoAxioms[1])
D.specify(1,'a','0')
D.existence(2,'(0+0)','a')
print(D.write_theorems_and_descriptions())
