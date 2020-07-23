def kleene_finite(S,n):
    if n == 0:
        yield ""
    else:
        unique = set([])
        for v in kleene_finite(S,n-1):
            for s in S:
                if v+s not in unique:
                    unique.add(v+s)
                    yield v+s

def kleene_star(S):
    unique = set([])
    
    ctr = 0
    while True:
        for s in kleene_finite(S,ctr):
            if s not in unique:
                unique.add(s)
                yield s
        ctr += 1
    

if __name__ == '__main__':
    
    S = ['a','ab','ba','cc']
    for i in range(4):
        K = [k for k in kleene_finite(S,i)]
        print(f"V_{i} = {K}")
    
    for n,s in enumerate(kleene_star(S)):
        print(s)
        if n > 30:
            break