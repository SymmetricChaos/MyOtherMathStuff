import re
from Utils.StringManip import left_string
# ∧∨⊃∃∀⋅

# Build statements in Typographical Number Theory
def EXISTS(a,x=""):
	if is_var(a):
		return f"∃{a}:{x}"
	else:
		raise Exception(f"Existential quantifier does not apply to {a}")
	
def FOR_ALL(a,x=""):
	if is_var(a):
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



# Translate to "plain English"
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



# Functions for splitting strings to be used for checking well formedness
def split_add_mul(x):
    L,lo,hi = left_string(x,"(","⋅+")
    R = x[hi+2:-1]
    return L,R

def split_eq(x):
    return x.split("=",maxsplit=1)
    


# Simplest atoms
def is_var(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def is_num(x):
    while x[0] == "S":
        x = x[1:]
    if x == "0" or is_var(x):
        return True
    return False

def is_pure_num(x):
    while x[0] == "S":
        x = x[1:]
    if x == "0":
        return True
    return False

# Variables and numbers are terms
# For more complex expressions split additions and multiplication until a lowest
# level is reached.
def is_term(x):
    if is_var(x) or is_num(x):
        return True
    else:
        # Before splitting we strip out S from the left
        # This prevents an error is there is a chain of Ss outside the parentheses
        # Removing S cannot turn a non-term into a term so there is no risk here
        while x[0] == "S":
            x = x[1:]
        L,R = split_add_mul(x)
        return is_term(L) and is_term(R)

def is_atom(x):
    if "=" not in x:
        return False
    else:
        L,R = x.split("=",maxsplit=1)
        return is_term(L) and is_term(R)






if __name__ == '__main__':
    zero = "0"
    one = SUCC(zero)
    two = SUCC(one)
    b = "b"
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
    
    print("\n\n\nTranslation puzzles from GEB\n")
    for i in ["~∀c:∃b:(SS0⋅b)=c",
              "∀c:~∃b:(SS0⋅b)=c",
              "∀c:∃b:~(SS0⋅b)=c",
              "~∃b:∀c:(SS0⋅b)=c",
              "∃b:~∀c:(SS0⋅b)=c",
              "∃b:∀c:~(SS0⋅b)=c"]:
        print(f"{i}\n{translate_TNT(i)}\n\n")
    
    print("\n\n\nChecking well-formedness")
    terms = ["0","b","SSa'","(S0⋅(SS0+c))","S(Sa⋅(Sb⋅Sc))"]
    atoms = ["S0=0","(SS0+SS0)=SSSS0","S(b+c)=((c⋅d)⋅e)"]

    parts_list = [terms,atoms]
    check_list = [is_term,is_atom]
    name_list = ["Terms","Atoms"]
    
    for parts,check,name in zip(parts_list,check_list,name_list):
        print(f"\n{name}")
        for p in parts:
            if check(p):
                print(f"{p:<16} TRUE")
            else:
                print(f"{p:<16} FALSE")