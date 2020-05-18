import re
from Utils.StringManip import bracket_matching

# ∧∨⊃

# Determine if the input is an atomic well-formed string
def is_atom(x):
    if re.match("^~*[PQR]\'*$",x):
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

def left_string(x):
    braks = bracket_matching(x,"<","⊃∧∨",overlap=True,inner=True,warn=False)
    for i in braks:
        if i[1] == 1:
            return i



# Doesn't work because it doesn't detect the "level" of nested brackets
def is_well_formed(x):
    
    if is_atom(x):
        print(f"{x} is an atom")
        return True
    elif re.match("^~*[PQR]'*[∧∨⊃]~*[PQR]'*>$",x):
        print(f"{x} is a simple formula")
        return True
    else:
        #split left and right and try again
        #remember to check that new substring starts in a valid way with ~ or <
        while x[0] == "~":
            x = x[1:]
        try:
            L,lo,hi = left_string(x)
        except:
            print(f"{x} is invalid")
            return False
        R = x[hi+2:-1]
        
        print(f"recur on {L} and {R}")
        
        ltrue = is_well_formed(L)
        rtrue = is_well_formed(R)
        
        return ltrue and rtrue





if __name__ == '__main__':

    P = "P"
    Qp = "Q'"
    print(P)
    print(NOT(P))
    print(NOT(NOT(P)))
    print(Qp)
    print(AND(P,NOT(Qp)))
    
    
    ss = ["<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>",
          "<~<P∧~Q'∧R>∨<~<~P∧R>⊃Q'>>",
          "<~<P∧~Q'∧R><~<~P∧R>⊃Q'>>"]
    print("\n")
    for s in ss:
        print()
        print(s)
        print(is_well_formed(s))