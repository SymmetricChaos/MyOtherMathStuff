def LSystem(state,rule,iters=3):
    print(state)
    for i in range(iters):
        t = ""
        for l in state:
            t += rule(l)
        print(t)
        state = t
        

def func1(S):
    if S == "A":
        return "AB"
    if S == "B":
        return "A"

LSystem("A",func1)
print()

def func2(S):
    if S == "A":
        return "AA"
    if S == "B":
        return "A[B]B"
    else:
        return S

LSystem("B",func2)