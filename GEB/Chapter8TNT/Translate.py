import re
from Utils.StringManip import bracket_matching
from GEB.Chapter8TNT.Properties import starts_quantifier

# Translate to "plain English"
def translate(s):
    
    # Translate existential quantifier
    E = re.search("∃[a-z]\'*:",s)
    while E != None:
        lo, hi = E.span()
        inside = s[lo+1:hi-1]
        left = s[:lo]
        right = s[hi:]
        if starts_quantifier(right):
            s = f"{left} there exists {inside} and {right} "
        else:
            s = f"{left} there exists {inside} such that {right}"
        E = re.search("∃[a-z]\'*:",s)

    # Translate universal quantifier
    A = re.search("∀[a-z]\'*:",s)
    while A != None:
        lo, hi = A.span()
        inside = s[lo+1:hi-1]
        left = s[:lo]
        right = s[hi:]
        if starts_quantifier(right):
            s = f"{left} for all {inside} and {right} "
        else:
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