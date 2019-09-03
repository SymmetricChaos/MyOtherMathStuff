## Context free L-systems


def LSystem(state,rule,iters=3):
    yield state
    for i in range(iters):
        t = ""
        for l in state:
            t += rule(l)
        state = t
        yield state
        