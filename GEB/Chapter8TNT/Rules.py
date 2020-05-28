from GEB.Chapter8TNT.Properties import is_var, get_vars, get_free_vars, is_num, \
                                       get_bound_vars, is_term, is_atom
from GEB.Chapter8TNT.StripSplit import split_eq, replace_var


# Build statements in Typographical Number Theory
def EXISTS(x,a):
    if is_var(a):
        if a in get_free_vars(x):
            return f"∃{a}:{x}"
        else:
            raise Exception(f"{a} is already quantified in {x}")
    else:
        raise Exception(f"Existential quantifier does not apply to {a}")
	
def FOR_ALL(x,a):
    if is_var(a):
        if a in get_free_vars(x):
            return f"∀{a}:{x}"
        else:
            raise Exception(f"{a} is already quantified in {x}")
    else:
        raise Exception(f"Existential quantifier does not apply to {a}")

def AND(x,y):
	return f"<{x}∧{y}>"
	
def OR(x,y):
	return f"<{x}∨{y}>"
	
def IMPLIES(x,y):
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

### Rules of Production ###
# Change a general statement into a specifice assertion
def specify(x,u,s):
    if f"∀{u}:" in x:
        # Eliminate the quantifer
        x = x.replace(f"∀{u}:","")
        
        # Check if replacement is allowed
        x_b_vars = get_bound_vars(x)
        s_vars = get_vars(s)
        for sv in s_vars:
            for xbv in x_b_vars:
                if sv in xbv:
                    raise Exception(f"{sv} is bound in {x}")
        
        x = replace_var(x,u,s)
        return x
    
    else:
        raise Exception(f"{u} is not bound in {x}")


# Assert that a statement about a free variable is universally true
def generalize(x,u):
    f_vars = get_free_vars(x)
    if u in f_vars:
        return FOR_ALL(x,u)
    else:
        raise Exception(f"{u} is not free in {x}")

# MAKE THESE INTO ONE FUNCTION WITH SOME OPTIONS
# Rephrase the existential quantifier as a universal quantifer
def interchange_EA(x,u):
    E = f"~∃{u}:"
    A = f"∀{u}:~"
    return x.replace(E,A)

# Rephrase the universal quantifier as an existential quantifer
def interchange_AE(x,u):
    E = f"~∃{u}:"
    A = f"∀{u}:~"
    return x.replace(A,E)

# CHECK HOW THESE INTERACT WITH NEGATIONS
def successor(x):
    if is_atom(x):
        left, right = split_eq(x)
        return f"S{left}=S{right}"
    else:
        raise Exception(f"{x} is not an equality of two terms")

def predecessor(x):
    if is_atom(x):
        left, right = split_eq(x)
        if left[0] != "S":
            raise Exception(f"{left} has no predecessor")
        if right[0] != "S":
            raise Exception(f"{right} has no predecessor")
            
        return f"{left[1:]}={right[1:]}"
    else:
        raise Exception(f"{x} is not an equality of two terms")

def existence(x,u,v):
    if is_term(u):
        if v in get_bound_vars(x):
            raise Exception(f"{v} is already bound in {x}")
        else:
            x = replace_var(x,u,v)
            return EXISTS(x,v)
    else:
        raise Exception(f"{u} is not a valid terms")

def symmetry(x):
    if is_atom(x):
        left, right = split_eq(x)
        return f"{right}={left}"
    else:
        raise Exception(f"{x} is not an equality of two terms")

def transitivity(x,y):
    # Helpful errors
    if not is_atom(x):
        raise Exception(f"{x} is not an equality of two terms")
    if not is_atom(y):
        raise Exception(f"{y} is not an equality of two terms")

    # Split and recombine
    leftx, rightx = split_eq(x)
    lefty, righty = split_eq(y)
    if rightx == lefty:
        return f"{leftx}={righty}"
    else:
        raise Exception(f"{x} and {y} do not form a transitive statement")
        
def induction(x,u,T):
    if u not in get_free_vars(x):
        raise Exception(f"{u} is not free in {x}")
    
    xS = replace_var(x,u,f"S{u}")
    x0 = replace_var(x,u,"0")
    
    if f"∀{u}:<{x}⊃{xS}>" in T and f"{x0}" in T:
        return f"∀{u}:{x}"
    else:
        raise Exception(f"Theorems do not allow induction on {x}")