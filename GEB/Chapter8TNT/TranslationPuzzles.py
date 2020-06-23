from GEB.Chapter8TNT.Rules import *
from GEB.Chapter8TNT.Translate import translate
from GEB.Chapter8TNT.Properties import is_well_formed

divisibility = "∃c:(a⋅c)=b"
is_even = "∃a:(a⋅SS0)=b"
greater_than = "∃c:<(a+c)=b∧~a=b>"
prime = "∀a:~∃c:(SSa⋅SSc)=b"
square = "∃a:(a⋅a)=b"
square_root = "∃b:(a⋅a)=b"
power_of_two = "<∃c:(a⋅c)=b⊃∃d:(d⋅SS0)=a>"



explanations = ["b is divisible by a if",
                "b is even if",
                "b is greather than a if",
                "b is prime if",
                "b is square if",
                "a is the square root of b if",
                "b is a power of two if"]

theorems = [divisibility,
            is_even,
            greater_than,
            prime,
            square,
            square_root,
            power_of_two]



for ex,th in zip(explanations,theorems):
    if not is_well_formed(th):
        print(f"{th} is not well formed!")
        break
    print(ex,translate(th))
    print(th)
    print()