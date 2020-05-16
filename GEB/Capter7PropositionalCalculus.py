import re

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

def bracket_matching(x):
    # Positions of left brackets
    left = []
    # 
    spans = []
    for pos in range(len(x)):
        if x[pos] == "<":
            left.append(pos)
        if x[pos] == ">":
            try:
                spans.append( (left.pop(),pos) )
            except:
                raise Exception(f"Too many right brackets")
    
    if len(left) != 0:
        raise Exception(f"Too many left brackets")

    return spans

if __name__ == '__main__':

    P = "P"
    Qp = "Q'"
    print(P)
    print(NOT(P))
    print(NOT(NOT(P)))
    print(Qp)
    print(NOT(Qp))
    print(AND(P,NOT(Qp)))
    
    print("\nTo decompose well-formed strings we need to be able to find bracketed sections. Consider the well-formed string below.")
    s = OR(NOT(AND(P,NOT(Qp))),IF(NOT(NOT(P)),Qp))
    print(s)
    print("The bracketed parts of the string area:")
    braks = bracket_matching(s)
    for lo,hi in braks:
        print(s[lo:hi+1])