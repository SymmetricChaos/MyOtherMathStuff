# Need to divide the state into pieces that respect
# parentheses

def rewrite(state,rule,iters=3):
    yield state
    for i in range(iters):
        t = ""
#        for l in state:
#            t += rule(l)
        state = t
        yield state
        
def peano_rule(S):
    """
    A+0 -> A
    A + S(B) -> S(A+B)
    A*0 -> 0
    A * S(B) -> A + A*B
    """
    pass