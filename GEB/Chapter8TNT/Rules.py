from GEB.Chapter8TNT.Properties import is_var, get_vars, get_free_vars, is_num, \
                                       get_bound_vars, is_term, is_atom, is_well_formed
from GEB.Chapter8TNT.StripSplit import split_eq, replace_var, replace_var_nth, \
                                       split


# Build abitrary statements in Typographical Number Theory
def EXISTS(x,var):
    if is_var(var):
        if var in get_free_vars(x):
            return f"∃{var}:{x}"
        else:
            if var in get_bound_vars(x):
                raise Exception(f"Quantification Error: {var} is already quantified in {x}")
            else:
                raise Exception(f"Quantification Error: {var} does not exist in {x}")
    else:
        raise Exception(f"Quantification Error: {var} is not a variable")
	
def FOR_ALL(x,var):
    if is_var(var):
        if var in get_free_vars(x):
            return f"∀{var}:{x}"
        else:
            if var in get_bound_vars(x):
                raise Exception(f"Quantification Error: {var} is already quantified in {x}")
            else:
                raise Exception(f"Quantification Error: {var} does not exist in {x}")
    else:
        raise Exception(f"Quantification Error: {var} is not a variable")

def AND(x,y):
    if not is_well_formed(x):
        raise Exception(f"Logical Error: {x} is not a well-formed formula")
    if not is_well_formed(y):
        raise Exception(f"Logical Error: {y} is not a well-formed formula")
    return f"<{x}∧{y}>"
	
def OR(x,y):
    if not is_well_formed(x):
        raise Exception(f"Logical Error: {x} is not a well-formed formula")
    if not is_well_formed(y):
        raise Exception(f"Logical Error: {y} is not a well-formed formula")
    return f"<{x}∨{y}>"
	
def IMPLIES(x,y):
    if not is_well_formed(x):
        raise Exception(f"Logical Error: {x} is not a well-formed formula")
    if not is_well_formed(y):
        raise Exception(f"Logical Error: {y} is not a well-formed formula")
    return f"<{x}⊃{y}>"
	
def NOT(x):
    if not is_well_formed(x):
        raise Exception(f"Logical Error: {x} is not a well-formed formula")
    return f"~{x}"

def SUCC(x):
    if not is_term(x):
        raise Exception(f"Successor Error: Cannot have successor of {x}")
    return f"S{x}"
  
def ADD(x,y):
    if not is_term(x):
        raise Exception(f"Arithmetic Error: {x} is not a term so it cannot be added")
    if not is_term(y):
        raise Exception(f"Arithmetic Error: {y} is not a term so it cannot be added")
    return f"({x}+{y})"

def MUL(x,y):
    if not is_term(x):
        raise Exception(f"Arithmetic Error: {x} is not a term so it cannot be multiplied")
    if not is_term(y):
        raise Exception(f"Arithmetic Error: {y} is not a term so it cannot be multiplied")
    return f"({x}⋅{y})"

def EQ(x,y):
    if not is_term(x):
        raise Exception(f"Arithmetic Error: {x} is not a term so it cannot be part of an equality")
    if not is_term(y):
        raise Exception(f"Arithmetic Error: {y} is not a term so it cannot be part of an equality")
    return f"{x}={y}"

###############################
##### Rules of Production #####
###############################

# Change a general statement into a specifice assertion
def specify(x,var,term):
    if not is_term(term):
        raise Exception(f"Specification Error: {term} is not a term")
    if not is_var(var):
        raise Exception(f"Specification Error: {var} is not a vaiable")
    if f"∀{var}:" in x:
        # Eliminate the quantifer
        x = x.replace(f"∀{var}:","")
        
        # Check if replacement is allowed
        x_b_vars = get_bound_vars(x)
        term_vars = get_vars(term)
        for tv in term_vars:
            for xbv in x_b_vars:
                if tv in xbv:
                    raise Exception(f"Specification Error: {tv} is bound in {x}")
        
        x = replace_var(x,var,term)
        return x
    else:
        raise Exception(f"Specification Error: {var} is not universally quantified in {x}")


# Assert that a statement about a free variable is universally true
def generalize(x,var):
    if var in get_free_vars(x):
        return FOR_ALL(x,var)
    else:
        raise Exception(f"Generalization Error: {var} is not free in {x}")


# Rephrase the existential quantifier as a universal quantifer
def interchange_EA(x,var,n):
    if is_var(var):
        E = f"~∃{var}:"
        A = f"∀{var}:~"
        if E not in x:
            raise Exception(f"Interchange Error: the string ~∃{var}: does not exist in {x}")

        return replace_var_nth(x,E,A,n)
    else:
        raise Exception(f"Interchange Error: {var} is not variable")


# Rephrase the universal quantifier as an existential quantifer
def interchange_AE(x,var,n):
    if is_var(var):
        E = f"~∃{var}:"
        A = f"∀{var}:~"
        if A not in x:
            raise Exception(f"Interchange Error: the string ~∃{var}: does not exist in {x}")
        return replace_var_nth(x,A,E,n)
    else:
        raise Exception(f"Interchange Error: {var} is not variable")


def successor(atom):
    if is_atom(atom):
        left, right = split_eq(atom)
        return EQ(SUCC(left),SUCC(right))
    else:
        raise Exception(f"Successor Error: {atom} is not an atom")


def predecessor(atom):
    if is_atom(atom):
        left, right = split_eq(atom)
        if left[0] != "S":
            raise Exception(f"Predecessor Error: {left} has no predecessor")
        if right[0] != "S":
            raise Exception(f"Predecessor Error: {right} has no predecessor")
            
        return EQ(left[1:],right[1:])
    else:
        raise Exception(f"Predecessor Error: {atom} is not an atom")


def existence(x,term,var):
    if not is_var(var):
        raise Exception(f"Existence Error: {var} is not a valid variable")
    if is_term(term):
        if var in get_bound_vars(x):
            raise Exception(f"Existence Error: {var} is already bound in {x}")
        else:
            x = replace_var(x,term,var)
            return EXISTS(x,var)
    else:
        raise Exception(f"Existence Error: {term} is not a valid term")


def symmetry(atom):
    if is_atom(atom):
        left, right = split_eq(atom)
        return EQ(right,left)
    else:
        raise Exception(f"Symmetry Error: {atom} is not an atom")


def transitivity(atom1,atom2):
    if not is_atom(atom1):
        raise Exception(f"Transitivity Error: {atom1} is not an atom")
    if not is_atom(atom2):
        raise Exception(f"Transitivity Error: {atom2} is not an atom")

    leftx, rightx = split_eq(atom1)
    lefty, righty = split_eq(atom2)
    if rightx == lefty:
        return EQ(leftx,righty)
    else:
        raise Exception(f"Transitivity Error: {atom1} and {atom2} do not form a transitive statement")
        
        
def induction(x,var,T):
    if var not in get_free_vars(x):
        raise Exception(f"Induction Error: {var} is not free in {x}")
    
    xS = replace_var(x,var,f"S{var}")
    x0 = replace_var(x,var,"0")
    
    if f"∀{var}:<{x}⊃{xS}>" in T and f"{x0}" in T:
        return FOR_ALL(x,var)
    else:
        raise Exception(f"Induction Error: Theorems do not allow induction on {x}")

