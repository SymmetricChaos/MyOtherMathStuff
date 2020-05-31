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
            s = f"{left} for all {inside} it is the case that {right} "
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
        s = f"{left}({num} + {ctr}){right}"
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

        s = f"{left}({num} + {ctr}{right}"
        N = re.search("S+\(",s)

    # Simple translations
    symbol = ["~","+","⋅","=","⊃","∨","∧","<",">"]
    translation = [" it is false that ",
                   " + ", " ⋅ ",
                   " = ", ") implies that (",
                   ") or (", ") and (", "(", ")"]
    
    # Fix spacing issues
    for sym,t in zip(symbol,translation):
        s = s.replace(sym,t)
        
    while "  " in s:
        s = s.replace("  "," ")
        
    if s[0] == " ":
        s = s[1:]
    
    return s

def translate_arithmetic(s):
    
    disallowed = re.findall("[b-z]",s)
    if disallowed != []:
        raise Exception(f"Austere TNT requires for arithmetic coding. The symbold {disallowed} are disallowed.")
    
    D = {"0":"666", "S":"123", "=":"111", "+":"123",
         "⋅":"236", "(":"362", ")":"323", "<":"212",
         ">":"213", "[":"312", "a":"262", "'":"163",
         "∧":"161", "∨":"616", "⊃":"633", "~":"223",
         "∃":"333", "∀":"626", ":":"636"}
    
    for sym,codon in D.items():
        s = s.replace(sym,codon)
    
    return int(s)



if __name__ == '__main__':
    # Quick tests
    strings = ["~S0=0","SSSc'=d''","∀e:<<e+0=0∧0+b=0>∨y⋅0=0>","∀a:∀a':(a+Sa')=S(a+a')"]
    for s in strings:
        print(f"{s}\n{translate(s)}")
        try:
            print(f"{translate_arithmetic(s)}\n")
        except:
            print()