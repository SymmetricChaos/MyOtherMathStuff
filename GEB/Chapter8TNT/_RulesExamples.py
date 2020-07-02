from Rules import specify, successor, predecessor, generalize, existence, transitivity, symmetry
from Deduction import PeanoAxioms

print("\n\nRule of Specification")
print(f"{PeanoAxioms[1]} ⟹ {specify(PeanoAxioms[1],'a','Sa')}")
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


print("\n\n\nRule of Symmetry")
symm_example1 = "(a+0)=a"
print(f"{symm_example1}")
print(f"{symmetry(symm_example1)}")