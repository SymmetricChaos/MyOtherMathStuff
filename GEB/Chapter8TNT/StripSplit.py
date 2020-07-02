import re
from Utils.StringManip import left_string

# CANNOT IMPORT FROM PROPERTIES

# Functions for splitting strings to be used for checking well formedness

def split(x,left,right):
    L,lo,hi = left_string(x,left,right,inner=True,warn=False)
    R = x[hi+2:-1]
    return L,R

def split_add_mul(x):
    return split(x,"(","⋅+")

def split_logical(x):
    return split(x,"<","∧∨⊃")

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
def strip_neg_qaunt(x):
    x = strip_neg(x)
    m = re.match("^[∀∃][a-z]\'*:",x)
    while m:
        span = m.span()
        x = x[span[1]:]
        x = strip_neg(x)
        m = re.match("^[∀∃][a-z]\'*:",x)
    return x



# Need this because ordinary replacement will replace the a in a'
def replace_var(x,pattern,replacement):
    
    if pattern not in x:
        raise Exception(f"Replacement Error: {pattern} not in {x}")
    
    left = ""
    pattern = re.escape(pattern)
    f = re.search(pattern,x)

    # While a possible match is found in x
    while f != None:
        # Get the upper and lower limits of the match
        lo,hi = f.span()
        # If the upper is not the end of the string
        if hi != len(x):
            # If the character immediately after the match is ' (meaning we only have part of a variable)
            # Then store the left half half and continue working with the right half
            if x[hi] == "'":
                left += x[:hi]
                x = x[hi:]
            # Otherwise append the the replacement to the left half, ignoring the matched section
            # and continue working with the right half
            else:
                left += x[:lo] + replacement
                x = x[hi:]
        # If we did reach the end of the string, ignoring the matched section
        # and continue working with the right half
        else:
            left += x[:lo] + replacement
            x = x[hi:]
        f = re.search(pattern,x)
    return left+x


def replace_var_nth(x,pattern,replacement,n):
    
    if pattern not in x:
        raise Exception(f"Replacement Error: {pattern} not in {x}")
    
    left = ""
    pattern_esc = re.escape(pattern)
    f = re.search(pattern_esc,x)
    ctr = 1

    while f != None:
        
            
        
        lo,hi = f.span()
        if ctr == n:
            if hi != len(x):
                if x[hi] == "'":
                    left += x[:hi]
                    x = x[hi:]
                else:
                    left += x[:lo] + replacement
                    x = x[hi:]
            else:
                left += x[:lo] + replacement
                x = x[hi:]
            return left+x
        else:
            left += x[:hi]
            x = x[hi:]
        f = re.search(pattern_esc,x)
        ctr += 1
    
    raise Exception(f"Replacement Error: {pattern} does not appear {n} times in {x}")
    


if __name__ == '__main__':
    
    S = "∀c:<∀d:(d+Sc)=(Sd+c)⊃∀d:(d+SSc)=(Sd+Sc)>"
    print(S)
    print(replace_var(S,"∀d","∀z"))
    
    print(split_add_mul("S(d+b)"))