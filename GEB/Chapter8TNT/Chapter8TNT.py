from GEB.Chapter8TNT.Properties import is_var, get_vars, get_free_vars, is_num, \
                                       get_bound_vars, get_quants, is_term, is_atom, \
                                       is_compound
from GEB.Chapter8TNT.Translate import translate
from GEB.Chapter8TNT.StripSplit import split_eq
# ∧∨⊃∃∀⋅

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

# Rules of Production
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
        
        x = x.replace(u,s)
        return x
    
    else:
        raise Exception(f"{u} is not bound in {x}")

# DOUBLE CHECK RESTRICTION
def generalize(x,u):
    f_vars = get_free_vars(x)
    if u in f_vars:
        return FOR_ALL(x,u)
    else:
        raise Exception(f"{u} is not free in {x}")

# MAKE THESE INTO ONE FUNCTION WITH SOME OPTIONS
def interchange_EA(x,u):
    E = f"~∃{u}:"
    A = f"∀{u}:~"
    return x.replace(E,A)

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
            x = x.replace(u,v)
            return EXISTS(x,v)
    else:
        raise Exception(f"{u} is not a valid terms")

def symmetry(x):
    if is_atom(x):
        left, right = split_eq(x)

        return f"{right}={left}"
    else:
        raise Exception(f"{x} is not an equality of two terms")



if __name__ == '__main__':

    print("Build some statements of Typographical Number Theory")
    zero = "0"
    one = SUCC(zero)
    two = SUCC(one)
    b = "b"
    sq = MUL(b,b)
    sq_2 = EQ(sq,two)
    ex_sq_2 = EXISTS(sq_2,b)
    not_ex_sq_2 = NOT(ex_sq_2)
    print(zero)
    print(one)
    print(two)
    print(b)
    print(sq)
    print(sq_2)
    print(ex_sq_2)
    print(not_ex_sq_2)
    
    
    print("\n\n\nTranslation puzzles from GEB\n")
    for i in ["~∀c:∃b:(SS0⋅b)=c",
              "∀c:~∃b:(SS0⋅b)=c",
              "∀c:∃b:~(SS0⋅b)=c",
              "~∃b:∀c:(SS0⋅b)=c",
              "∃b:~∀c:(SS0⋅b)=c",
              "∃b:∀c:~(SS0⋅b)=c"]:
        print(f"{i}\n{translate(i)}\n")
    
    
    open_formula = "<∀b:d'-b∧~c=c>"
    print(f"\n\nVariables and quantifiers extracted from {open_formula}")
    print(f"Variables used {get_vars(open_formula)}")
    print(f"Quantifications used {get_quants(open_formula)}")
    print(f"Bound variables {get_bound_vars(open_formula)}")
    print(f"Free variables {get_free_vars(open_formula)}")
    

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
                print(f"{p:<{l}} {translate(p)}")
            else:
                print(f"{p:<{l}} ERROR")
    
    
    Pax1 = "∀a:~Sa=0"
    Pax2 = "∀a:(a+0)=a"
    Pax3 = "∀a:∀b:(a+Sb)=S(a+b)"
    Pax4 = "∀a:(a⋅0)=0"
    Pax5 = "∀a:∀b:(a⋅Sb)=((a⋅b)+a)"
    peano_axioms = [Pax1,Pax2,Pax3,Pax4,Pax5]
    print("\n\n\nAxioms of Peano Arithmetic")
    for i in peano_axioms:
        print(f"{i}\n{translate(i)}\n")
    
    
    print("\n\nExample Specifications of Peano Arithmetic")
    print(f"{Pax1} ⟹ {specify(Pax1,'a','0')}")
    print(f"{Pax2} ⟹ {specify(Pax2,'a','S0')}")
    print(f"{Pax3} ⟹ {specify(Pax3,'a','(c+d)')}")
    print(f"{Pax4} ⟹ {specify(Pax4,'a','(S0⋅0)')}")
    print(f"{Pax5} ⟹ {specify(Pax5,'b','(S0+b)')}")
    
    
    print("\n\n\nRules of Successorship")
    succ_example = "SSS0=S(S0+S0)"
    print(f"{succ_example} ⟹ {successor(succ_example)}")
    print(f"{succ_example} ⟹ {predecessor(succ_example)}")
    
    
    print("\n\n\nRule of Existence")
    print(f"{Pax1} ⟹ {existence(Pax1,'0','b')}")
    print(f"{Pax3} ⟹ {existence(Pax3,'Sb','c')}")
    