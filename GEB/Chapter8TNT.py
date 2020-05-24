import re
from Utils.StringManip import left_string, bracket_matching
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
        s = f"{left}there exists {inside} such that {right}"
        E = re.search("∃[a-z]\'*:",s)

    # Translate universal quantifier
    A = re.search("∀[a-z]\'*:",s)
    while A != None:
        lo, hi = A.span()
        inside = s[lo+1:hi-1]
        left = s[:lo]
        right = s[hi:]
        s = f"{left} for all {inside} {right} "
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
        s = f"{left}{ctr}{right} "
        N = re.search("S+0",s)
    
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
        s = f"{left}({num} plus {ctr}){right}"
        N = re.search("S+[a-z]\'*",s)
        
    # Translate even more generalized additions that remain
    # Needs to use a bracket matching system to isolate correctly
    N = re.search("S+\(",s)
    while N != None:
        braks = bracket_matching(s,"(",")")
        span = N.span()
        for i in braks:
            if i[1] == span[1]-1:
                num, lo, hi = i
                break

        left = s[:lo]
        right = s[hi:]

        ctr = 0
        if left != "":
            while left[-1] == "S":
                ctr += 1
                left = left[:-1]
                if left == "":
                    break

        s = f"{left}({num} plus {ctr}{right}"
        N = re.search("S+\(",s)

    # Simple translations
    symbol = ["~","+","⋅","=","⊃","∨","∧","<",">"]
    translation = [" it is false that ",
                   " plus ", " times ",
                   " equals ", " implies that ",
                   " or ", " and ", "", ""]
    
    # Fix spacing issues
    for sym,t in zip(symbol,translation):
        s = s.replace(sym,t)
        
    while "  " in s:
        s = s.replace("  "," ")
        
    if s[0] == " ":
        s = s[1:]
    
    return s



# Functions for splitting strings to be used for checking well formedness
def split_add_mul(x):
    L,lo,hi = left_string(x,"(","⋅+")
    R = x[hi+2:-1]
    return L,R

def split_logical(x):
    L,lo,hi = left_string(x,"<","∧∨⊃")
    R = x[hi+2:-1]
    return L,R

def split_eq(x):
    return x.split("=",maxsplit=1)

# Strip out ~ and S
def strip_neg(x):
    while x[0] == "~":
        x = x[1:]
    return x

def strip_succ(x):
    while x[0] == "S":
        x = x[1:]
    return x

def strip_qaunt(x):
    x = strip_neg(x)
    m = re.match("^[∀∃][a-z]\'*:",x)
    while m:
        span = m.span()
        x = x[span[1]:]
        x = strip_neg(x)
        m = re.match("^[∀∃][a-z]\'*:",x)
    return x

# Get variables
def get_vars(x):
    v = re.findall("[a-z]\'*",x)
    return set(v)

#def get_free_vars(x):
#
#def get_bound_vars(x):



# Simplest atoms
def is_var(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def is_num(x):
    x = strip_succ(x)
    if x == "0" or is_var(x):
        return True
    return False

def is_pure_num(x):
    x = strip_succ(x)
    if x == "0":
        return True
    return False

# Variables and numbers are terms as are negations of them
def is_term(x):
    x = strip_neg(x)
    if is_var(x) or is_num(x):
        return True
    else:
        # Before splitting we strip out S from the left
        # This prevents an error is there is a chain of Ss outside the parentheses
        # Removing S cannot turn a non-term into a term so there is no risk here
        x = strip_succ(x)
        try:
            L,R = split_add_mul(x)
            return is_term(L) and is_term(R)
        except:
            return False

# Atoms are terms seperated by an equality
def is_atom(x):
    x = strip_neg(x)
    if "=" not in x:
        return False
    else:
        try:
            L,R = x.split("=",maxsplit=1)
            return is_term(L) and is_term(R)
        except:
            return False

# Compounds are the first level at which negation comes into play
# Since negation of atoms and terms also gives a valid formula we just strip
# out the negations before working with the formula
def is_compound(x):
    x = strip_neg(x)
    if is_atom(x) or is_term(x) or is_quantifier(x):
        return True
    else:
        try:
            L,R = split_logical(x)
            # Remove negatives and quantifiers
            L = strip_neg(L)
            L = strip_qaunt(L)
            # Remove negatives and quantifiers
            R = strip_neg(R)
            R = strip_qaunt(R)
            return is_compound(L) and is_compound(R)
        except:
            return False
        
def is_quantifier(x):
    x = strip_neg(x)
    if re.match("^[∀∃][a-z]\'*:$",x):
        return True
    return False
            

#def is_open(x):
#
#def is_closed(x):




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
    
    
    
    print("\n\n\nVariables extracted from ~∀c:∃b':(SS0⋅b')=c")
    print(get_vars("~∀c:∃b':(SS0⋅b')=c"))
    
    

    terms = ["0","b","SSa'","(S0⋅(SS0+c))","S(Sa⋅(Sb⋅Sc))"]
    atoms = ["S0=0","(SS0+SS0)=SSSS0","S(b+c)=(S(c⋅d)⋅e)"]
    compounds = ["<S0=0⊃∀c:~∃b:(b+b)=c>"]

    parts_list = [terms,atoms,compounds]
    check_list = [is_term,is_atom,is_compound]
    name_list = ["Terms","Atoms","Compound Formulas"]
    
    print("\n\n\nChecking well-formedness\nAll should be well-formed (but may be false)")
    for parts,check,name in zip(parts_list,check_list,name_list):
        print(f"\n{name}")
        l = max([len(p) for p in parts])
        for p in parts:
            if check(p):
                print(f"{p:<{l}} {translate_TNT(p)}")
            else:
                print(f"{p:<{l}} ERROR")
                
                