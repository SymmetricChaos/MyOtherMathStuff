from GEB.Chapter8TNT.Chapter8TNT import Deduction, PeanoAxioms

for i in PeanoAxioms:
    print(i)

# Prove that 0 = 0

A = Deduction(PeanoAxioms[1])
A.specify(1,'a','0')
A.symmetry(2)
A.transitivity(3,2)

print("\n\nProove 0=0")
print(A.write_theorems_and_descriptions())