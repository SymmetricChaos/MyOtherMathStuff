from GEB.Chapter8TNT.Rules import *
from GEB.Chapter8TNT.Translate import translate
from GEB.Chapter8TNT.Properties import is_well_formed

divisibility = "∃c:(a⋅c)=b"
is_even = "∃a:(a⋅SS0)=b"
greater_than = "∃c:(a+Sc)=b"
prime = "∀a:~∃c:(SSa⋅SSc)=b"
square = "∃a:(a⋅a)=b"
square_root = "∃b:(a⋅a)=b"
power_of_two = "∀a:<∃c:(a⋅c)=b⊃∃d:(d⋅SS0)=a>"
multiple_of_ten = "∃a:∃b:<(SS0⋅a)=c∧(SSSSS0⋅b)=c>"


explanations = ["b is divisible by a if",
                "b is even if",
                "b is greather than a if",
                "b is prime if",
                "b is square if",
                "a is the square root of b if",
                "b is a power of two if",
                "c is a multiple of ten if"]

theorems = [divisibility,
            is_even,
            greater_than,
            prime,
            square,
            square_root,
            power_of_two,
            multiple_of_ten]


print("Cast decision problems in terms of open statements of TNT\n\n")
for ex,th in zip(explanations,theorems):
    if not is_well_formed(th):
        print(f"{th} is not well formed!")
        break
    print(ex,translate(th))
    print(th)
    print()