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
    # Spans covered
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

    # output is list with the subsections and the spans
    out = []
    for lo,hi in spans:
        out.append((x[lo:hi+1],lo,hi))

    return out





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
    braks = bracket_matching(s)
    for i in braks:
        print(i[0])
