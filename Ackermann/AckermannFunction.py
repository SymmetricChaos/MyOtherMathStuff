from Utils.StringManip import innermost, left_string
import time

# Normal Ackermann function
def A(M,N):
    if M == 0:
        return N+1
    if N == 0:
        return A(M-1,1)
    return A(M-1,A(M,N-1))


# A version of the Ackermann function without explicit recursion
def A_loop(M,N):
    aux = []
    while True:
        if M == 0 and aux == []:
            return N+1
        elif M == 0 and aux != []:
            N += 1
            M = aux.pop()
        elif N == 0:
            M,N = M-1,1
        else:
            aux.append(M-1)
            M,N = M,N-1


# Explore what the expansion of the Ackermann function looks like
def A_expand_simple(M,N):
    if M == 0:
        return f"{N+1}"
    if N == 0:
        return f"A({M-1},1)"
    return f"A({M-1},A({M},{N-1}))"

def A_expand(M,N):
    S = f"A({M},{N})"
    yield S
    while "A" in S:
        bottom,_,_ = innermost(S,"A",")")[0]
        m = int(left_string(bottom,"(",",",inner=True)[0])
        n = int(left_string(bottom,",",")",inner=True)[0])
        bottom_ex = A_expand_simple(m,n)
        S = S.replace(bottom,bottom_ex)
        yield S


# Little aesthetic function showing the size of the stack
def A_wave(M,N,wait=.2):
    for S in A_expand(M,N):
        print("#"*S.count("A"))
        time.sleep(wait)


