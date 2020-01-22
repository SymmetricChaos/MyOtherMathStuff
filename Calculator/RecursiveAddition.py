# Addition by its recursive definition

def succ(n):
    return f"S({n})"

def pred(n):
    return n[2:-1]

def recursive_addition(a,b):
    if a == "0":
        return b
    elif b == "0":
        return a
    else:
        print(a,b)
        return succ(recursive_addition(a,pred(b)))

print(recursive_addition("S(S(0))","S(S(S(0)))"))
