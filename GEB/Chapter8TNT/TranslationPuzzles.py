from GEB.Chapter8TNT.Rules import *
from GEB.Chapter8TNT.Translate import translate

divisibility = EXISTS("a*c=b","c")
greater_than = EXISTS(AND("a+c=b","~a=b"),"c")
prime = FOR_ALL(NOT("∃c:SSa*SSc=b"),"a")

explanations = ["b is divisible by a if",
                "b is greather than a if",
                "b is prime if"]
theorems = [divisibility,
            greater_than,
            prime]



for ex,th in zip(explanations,theorems):
    print(ex,translate(th))
    print(th)
    print()