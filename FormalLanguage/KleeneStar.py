def kleene_finite(S,n):
    S = set(S)
    if n == 0:
        yield ""
    else:
        unique = set([])
        for v in kleene_finite(S,n-1):
            for s in S:
                if v+s not in unique:
                    unique.add(v+s)
                    yield v+s

#def kleene_star(S):
#    for s in S:


if __name__ == '__main__':
    
    for i in range(4):
        print([k for k in kleene_finite(['ab','ba','aa'],i)])
    