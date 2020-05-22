import re
from Utils.StringManip import bracket_matching


def EXISTS(a,x=""):
	if is_atom(a):
		return f"∃{a}:{x}"
	else:
		raise Exception(f"Existential quantifier does not apply to {a}")
	
def FOR_ALL(a,x=""):
	if is_atom(a):
		return f"∀{a}:{x}"
	else:
		raise Exception(f"Universal quantifier does not apply to {a}")

def AND(x,y):
	return f"<{x}∧{y}>"
	
def OR(x,y):
	return f"<{x}∨{y}>"
	
def IF(x,y):
	return f"<{x}⊃{y}>"
	
def NOT(x,):
	return f"~{x}"

def SUCC(x):
	if is_num(x):
		return f"S{x}"
	else:
		raise Exception(f"Cannot have successor of {x}")
  
def ADD(x,y):
	return f"({x}+{y})"

def MUL(x,y):
	return f"({x}⋅{y})"

def EQ(x,y):
	return f"{x}={y}"
	


# ∧∨⊃∃∀⋅
def is_atom(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def is_num(x):
    while x[0] == "S":
        x = x[1:]
    if x == "0" or is_atom(x):
        return True
    return False



#def translate_TNT(s):
#    re.findall("")



if __name__ == '__main__':
    zero = "0"
    one = SUCC(zero)
    two = SUCC(one)
    b = "b"
    sq = MUL(b,b)
    ex_sq = EXISTS(b,sq)
    ex_sq_2 = EQ(ex_sq,two)
    not_ex_sq_2 = NOT(ex_sq_2)
    print(zero)
    print(one)
    print(two)
    print(b)
    print(sq)
    print(ex_sq)
    print(ex_sq_2)
    print(not_ex_sq_2)
    