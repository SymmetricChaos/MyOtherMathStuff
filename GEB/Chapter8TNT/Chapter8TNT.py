from GEB.Chapter8TNT.Properties import get_vars, get_free_vars, \
                                       get_bound_vars, get_quants
from GEB.Chapter8TNT.Translate import translate, translate_arithmetic
from GEB.Chapter8TNT.Deduction import PeanoAxioms, AusterePeanoAxioms


print("\nTranslation puzzles from GEB\n")
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
