# Need to translate rules into regex
# Maybe not possible that way?

import re

def peano_rewrite(state,iters=3):
    """
    A + 0 -> A
    A + S(B) -> S(A + B)
    A * 0 -> 0
    A * S(B) -> A + A*B
    """
    yield state
    for i in range(iters):
        patterns     = [ " + 0" ]
        replacements = [ "" ]
        for pat,rep in zip(patterns,replacements):
            state = state.replace(pat,rep)
        yield state
        
for i in peano_rewrite("A + 0",2):
    print(i)