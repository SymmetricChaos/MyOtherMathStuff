import re
from GEB.Chapter8TNT.StripSplit import strip_succ, split_add_mul, \
                                       split_logical, strip_neg_qaunt

# Get variables
def get_vars(x):
    v = re.findall("[a-z]\'*",x)
    return set(v)

# Return all quantifications used
def get_quants(x):
    q = re.findall("[∀∃][a-z]\'*:",x)
    return set(q)

# Return all variables that appear in quantifications
def get_bound_vars(x):
    var = get_vars(x)
    quant = get_quants(x)
    bound = set([])
    for v in var:
        for q in quant:
            if v in q:
                bound.add(v)
                break
    return bound

def is_bound_var(x,var):
    for i in get_bound_vars(x):
        if i == var:
            return True
    return False

# Return all variables that don't appear in quantifications
def get_free_vars(x):
    var = get_vars(x)
    bvar = get_bound_vars(x)
    return var-bvar # using the setminus here

def is_free_var(x,var):
    for i in get_free_vars(x):
        if i == var:
            return True
    return False


def var_in_string(x,var):
    if len(x) <= len(var):
        return False
    
    else:
        # Check chunk by chunk
        for i in range(len(x)-len(var)+1):
            # If we've reached the end of the string then any match is fine
            if i+len(var) == len(x):
                if x[i:i+len(var)] == var:
                    return True
            # Otherwise only match if the next symbol is not '
            elif x[i+len(var)] != "'":
                if x[i:i+len(var)] == var:
                    return True
    return False


# Check that all variables that are quantified exist in the rest of the string
def is_well_quantified(x):
    V = get_vars(strip_neg_qaunt(x))
    Q = get_quants(x)
    Qvars = [q[1:-1] for q in Q]
    for qv in Qvars:
        exists = False
        for v in V:
            if qv == v:
                exists = True
                break
        if not exists:
            return False
    return True


#####################################
### Parts of Well-Formed Formulas ###
#####################################
    
def is_var(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def is_num(x):
    x = strip_succ(x)
    if x == "0":
        return True
    return False


# Variables and numbers are terms as are arithmetic of them
def is_term(x):
    
    if x[0] not in "0(Sabcdefghijklmnopqrstuvwxyz":
        return False
    
    # The successor of a term is still a term
    x = strip_succ(x)
    
    # All numbers and variables are terms
    if is_num(x) or is_var(x):
        return True
    else:
        try:
            L,R = split_add_mul(x)
            return is_term(L) and is_term(R)
        except:
            return False



############################
### Well-Formed Formulas ###
############################

# Atoms are terms seperated by an equality
# The negation of an atom is well-formed but it is not an atom
# This property is handled by is_compound and is_well_formed
def is_atom(x):
    if "=" not in x:
        return False
    else:
        try:
            L,R = x.split("=",maxsplit=1)
            return is_term(L) and is_term(R)
        except:
            return False


# Checks if a formula is a compound of atoms and/or terms
def is_compound(x):
    
    # If a formula is not well quantified it is not well formed and thus not
    # a valid compound
    if not is_well_quantified(x):
        return False
    
    x = strip_neg_qaunt(x)
    if is_atom(x) or is_term(x):
        return False
    else:
        try:
            L,R = split_logical(x)
            
            L_free_vars = get_free_vars(L)
            L_bound_vars = get_bound_vars(L)
            R_free_vars = get_free_vars(R)
            R_bound_vars = get_bound_vars(R)
            
            for v in L_free_vars:
                if v in R_bound_vars:
                    return False
                
            for v in R_free_vars:
                if v in L_bound_vars:
                    return False
            
            # Remove negatives and quantifiers from the left
            L = strip_neg_qaunt(L)
            # Remove negatives and quantifiers from the right
            R = strip_neg_qaunt(R)
            
            # Some clever logic. If both L and R are atoms return true
            # If only L is an atom return recur on R
            # If only R is an atom return recur on L
            # If neither then recur on both
            if is_atom(L):
                if is_atom(R):
                    return True
                return is_compound(R)
            
            if is_atom(R):
                if is_atom(L):
                    return True
                return is_compound(L)
                    
            return is_compound(L) and is_compound(R)
        except:
            return False


# Removing the leading quantifiers and negations can never change if a string
# is well formed
def is_well_formed(x):

    # Quickly give a useful error message for a severely malformed input
    invalid = set([])
    for char in x:
        if char not in "0S=+⋅()<>[]abcdefghijklmnopqrstuvwxyz'∧∨⊃~∃∀:":
            invalid.add(char)
    if len(invalid) != 0:
        raise Exception(f"Formula {x} contains these invalid characters:\n{invalid}")
    
    # If quantification is invalid the formula is not well formed
    if not is_well_quantified(x):
        return False
    
    # Otherwise get rid of negations and quantifications then check if the
    # results is a compound or an atom
    x = strip_neg_qaunt(x)
    if is_compound(x) or is_atom(x):
        return True
    return False
        

# Not checking well formedness but other properties
def is_open(x):
    var = get_vars(x)
    quant = get_quants(x)
    for v in var:
        for q in quant:
            if v in q:
                return False
    return True

def is_closed(x):
    return not is_open(x)





if __name__ == '__main__':
    
    bool_string = lambda x: "False" if x == 0 else "True"
    
    test_strings = ["a","b","a'''",                       # variables
                    "S0", "0", "Sq",                      # numbers
                    "(a+b)", "(z⋅x)", "(a+S(a⋅a))",        # terms
                    "a=a", "Sa=b",                        # atoms
                    "<~∃b:~a=b∧∀c:~a=c>","<~(a+b)=0⊃<a=b∨0=S0>>", #compunds of atoms
                    ]

    def test_vars():
        print("\nCheck if a string is a variable")
        for i in test_strings:
            print(f"{bool_string(is_var(i)):<5}  {i}")
            
    def test_nums():
        print("\nTest if a string is a numerak")
        for i in test_strings:
            print(f"{bool_string(is_num(i)):<5}  {i}")
    
    def test_terms():
        print("\nTest if a string is a term (every variable and numeral is a term)")
        for i in test_strings:
            print(f"{bool_string(is_term(i)):<5}  {i}")
            
    def test_atoms():
        print("\nTest if a string is an atom (an equality of two terms)")
        for i in test_strings:
            print(f"{bool_string(is_atom(i)):<5}  {i}")
    
    def test_compounds():
        print("\nTest if a string is a compound of well-formed formulas")
        for i in test_strings:
            print(f"{bool_string(is_compound(i)):<5}  {i}")
            
    def test_well_formed():
        print("\nTest if a string is a well-formed formulas (note that correctly formed terms are not well-formed formulas)")
        for i in test_strings:
            print(f"{bool_string(is_well_formed(i)):<5}  {i}")
    
    test_vars()
    test_nums()
    test_terms()
    test_atoms()
    test_compounds()
    test_well_formed()