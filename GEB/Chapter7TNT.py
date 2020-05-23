import re
# ∧∨⊃∃∀⋅

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



def translate_TNT(s):
    
    # Translate existential quantifier
    E = re.search("∃[a-z]\'*:",s)
    while E != None:
        lo, hi = E.span()
        inside = s[lo+1:hi-1]
        left = s[:lo]
        right = s[hi:]
        s = left + "there exists " + inside + " such that " + right
        E = re.search("∃[a-z]\'*:",s)

    # Translate universal quantifier
    A = re.search("∀[a-z]\'*:",s)
    while A != None:
        lo, hi = A.span()
        inside = s[lo+1:hi-1]
        left = s[:lo]
        right = s[hi:]
        s = left + "for all " + inside + " it is the case that " + right
        A = re.search("∀[a-z]\'*:",s)
    
    # Translate natural numbers
    N = re.search("S+0",s)
    while N != None:
        lo, hi = N.span()
        num = s[lo:hi]
        ctr = 0
        while num[0] == "S":
            ctr += 1
            num = num[1:]
        
        left = s[:lo]
        right = s[hi:]
        s = left + f"{ctr}" + right
        N = re.search("S*0",s)
    
    # Translate addition natural number addition of variables
    N = re.search("S+[a-z]\'*",s)
    while N != None:
        lo, hi = N.span()
        num = s[lo:hi]
        ctr = 0
        while num[0] == "S":
            ctr += 1
            num = num[1:]
        left = s[:lo]
        right = s[hi:]
        s = left + num + f"{ctr}" + right
        N = re.search("S*[a-z]\'*",s)
    
    # Simple translations
    s = s.replace("~","it is false that ")
    s = s.replace("+"," plus ")
    s = s.replace("⋅"," times ")
    s = s.replace("="," equals ")
    s = s.replace("⊃"," implies that ")
    s = s.replace("∧"," and ")
    s = s.replace("∨"," or ")

    return s





if __name__ == '__main__':
    zero = "0"
    one = SUCC(zero)
    two = SUCC(one)
    b = "b'"
    sq = MUL(b,b)
    sq_2 = EQ(sq,two)
    ex_sq_2 = EXISTS(b,sq_2)
    not_ex_sq_2 = NOT(ex_sq_2)
    print(zero)
    print(one)
    print(two)
    print(b)
    print(sq)
    print(sq_2)
    print(ex_sq_2)
    print(not_ex_sq_2)
    
    print(translate_TNT(not_ex_sq_2))