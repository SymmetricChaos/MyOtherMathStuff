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



if __name__ == '__main__':

    P = "P"
    Qp = "Q'"
    print(P)
    print(NOT(P))
    print(NOT(NOT(P)))
    print(Qp)
    print(NOT(Qp))
    print(AND(P,NOT(Qp)))
    print(NOT(AND(P,NOT(Qp))))
    print(IF(NOT(NOT(P)),Qp))
    print(OR(NOT(AND(P,NOT(Qp))),IF(NOT(NOT(P)),Qp)))