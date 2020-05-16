import re
from Utils.StringManip import bracket_matching

# ∧∨⊃

# Determine if the input is an atomic well-formed string
def is_atom(x):
    if re.match("^[PQR]\'*$",x):
        return True
    return False

# Create well-formed strings
def AND(x,y):
    return f"<{x}∧{y}>"

def OR(x,y):
    return f"<{x}∨{y}>"

def IF(x,y):
    return f"<{x}⊃{y}>"

def NOT(x):
    return f"~{x}"






if __name__ == '__main__':

    P = "P"
    Qp = "Q'"
    print(P)
    print(NOT(P))
    print(NOT(NOT(P)))
    print(Qp)
    print(AND(P,NOT(Qp)))
    
    print("\nTo decompose well-formed strings we need to be able to find bracketed sections. Consider the well-formed string below.")
    s = "<~<P∧~Q'>∨<~~<P∧R>⊃Q'>>"
    print(s)
    print("The bracketed parts of the string are:")
    braks = bracket_matching(s,"<>")
    for i in braks:
        print(i[0],i[1:3])
