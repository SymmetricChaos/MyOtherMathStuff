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
    return bracket_matching(x[1:-1],"<","⊃∧∨",overlap=True,inner=False)

def right_string(x):
    return bracket_matching(x[1:-1],"⊃∧∨",">",overlap=True,inner=False)

# Doesn't work because it doesn't detect the "level" of nested brackets
def is_well_formed(x):
    
    if is_atom(x):
        print("{x} is an atom")
        return True
    elif re.match("^~*[PQR]'*[∧∨⊃]~*[PQR]'*>$",x):
        print("{x} is a simple formula")
        return True
    else:
        #split left and right and try again
        pass





if __name__ == '__main__':

    P = "P"
    Qp = "Q'"
    print(P)
    print(NOT(P))
    print(NOT(NOT(P)))
    print(Qp)
    print(AND(P,NOT(Qp)))
    
    
    print("\n\n")
    s1 = "<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>"
    print(s1)
    print(left_string(s1))
    print(right_string(s1))