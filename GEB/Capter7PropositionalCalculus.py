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

# Doesn't work because it doesn't detect the "level" of nested brackets
def is_well_formed(x):
    
    if is_atom(x):
        return True
    elif re.match("^~*[PQR]'*[∧∨⊃]~*[PQR]'*>$",x):
#        print("{x} is a simple formula")
        return True
    else:
#        print("!")
        if re.match("^<.*[∧∨⊃].*>$",x):
#            print(re.match("^<.*[∧∨⊃].*>$",x))
            strings = bracket_matching(x[1:-1],"<>",overlap=False)
            sub_strings = strings
            print(f"\ntesting {x}")
            for s in sub_strings:
                print(s)
                if not is_well_formed(s[0]):
#                    print(f"{x} is not well-formed")
                    return False
            
            return True
        else:
#            print(f"{x} is not well-formed")
            return False





if __name__ == '__main__':

    P = "P"
    Qp = "Q'"
    print(P)
    print(NOT(P))
    print(NOT(NOT(P)))
    print(Qp)
    print(AND(P,NOT(Qp)))
    
    print("\nTo decompose well-formed strings we need to be able to find bracketed sections. Consider the well-formed string below.")
    s = "<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>"
    print(s)
    print("The bracketed parts of the string are:")
    braks = bracket_matching(s[1:-1],"<>",overlap=False)
    for i in braks:
        print(i[0],i[1:3])
    
    s1 = "<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>"
    s2 = "<R<~<~P∧R>⊃Q'>>"
    print("\n\n")
    print(f"{s1} {is_well_formed(s1)}, should be True")
    print(f"{s2} {is_well_formed(s2)}, should be False")
