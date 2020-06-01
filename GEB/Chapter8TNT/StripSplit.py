import re
from Utils.StringManip import left_string

# CANNOT IMPORT FROM PROPERTIES

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



# Functions for removing certain symbols
def strip_neg(x):
    while x != "" and x[0] == "~":
        x = x[1:]
    return x

def strip_succ(x):
    while x != "" and x[0] == "S":
        x = x[1:]
    return x

# Removes quantifiers and also strips out negatives in the chain
def strip_qaunt(x):
    x = strip_neg(x)
    m = re.match("^[∀∃][a-z]\'*:",x)
    while m:
        span = m.span()
        x = x[span[1]:]
        x = strip_neg(x)
        m = re.match("^[∀∃][a-z]\'*:",x)
    return x



# Need this because ordinary replacement will replace the a in a'
def replace_var(x,v,r):
    left = ""
    f = re.search(v,x)

    while f != None:
        lo,hi = f.span()
        if hi != len(x):
            if x[hi] == "'":
                left += x[:hi]
                x = x[hi:]
            else:
                left += x[:lo] + r
                x = x[hi:]
        else:
            left += x[:lo] + r
            x = x[hi:]
        f = re.search(v,x)
    return left+x