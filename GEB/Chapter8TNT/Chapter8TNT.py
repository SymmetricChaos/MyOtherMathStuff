from GEB.Chapter8TNT.Properties import is_well_formed
from GEB.Chapter8TNT.Translate import translate, translate_arithmetic
from GEB.Chapter8TNT.Deduction import PeanoAxioms, AusterePeanoAxioms


print("\n### Translation puzzles from GEB ###\n")
for i in ["~∀c:∃b:(SS0⋅b)=c",
          "∀c:~∃b:(SS0⋅b)=c",
          "∀c:∃b:~(SS0⋅b)=c",
          "~∃b:∀c:(SS0⋅b)=c",
          "∃b:~∀c:(SS0⋅b)=c",
          "∃b:∀c:~(SS0⋅b)=c"]:
    print(f"{i}\n{translate(i)}\n")


print("\n\n### Example Sentences from GEB ### \n")
english_form = ["5 is prime",
                "2 is not square",
                "35 is the sum of two cubes",
                "Not sum of positive cubes is a cube",
                "There are infinitely many primes",
                "Six is even"
               ]
TNT_form = ["~∃a:∃b:(SSa⋅SSb)=SSSSS0",
            "~∃b:(b⋅b)=SS0",
            "∃b:∃c:((b⋅(b⋅b))+(c⋅(c⋅c)))=SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS0",
            "~∀b:∀c:(a⋅(a⋅a))=((Sb⋅(Sb⋅Sb))+(Sc⋅(Sc⋅Sc)))",
            "∀a:∃b:∃c:<(a+Sc)=b∧~∃d:∃e:(SSd⋅SSe)=b>",
            "∃e:(SS0⋅e)=6"
           ]
for e,t in zip(english_form,TNT_form):
    if not is_well_formed(i):
        print(f"{t} is not a well-formed formula")
    else:
        print(f"{e}\n{t}\n{translate(t)}\n\n")



print("\n\n\n### Translated Axioms of Peano Arithmetic ###")
for i in PeanoAxioms:
    print(f"{i}\n{translate(i)}\n")

print("\n\n### Arithmetized Axioms of Peano Arithmetic ###")
for i in AusterePeanoAxioms:
    print(f"{i}\n{translate_arithmetic(i)}\n")
