import re
from Utils.StringManip import bracket_matching


# ∧∨⊃∃∀
def is_atom(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def exists(a):
    if is_atom(a):
        return f"∃{a}:"
    else:
        raise Exception(f"Existential quantifier does not apply to {a}")
    
def for_all(a):
    if is_atom(a):
        return f"∀{a}:"
    else:
        raise Exception(f"Universal quantifier does not apply to {a}")





if __name__ == '__main__':
    print(exists("k''"))