def reverse_polish(S):
    assert type(S) == str
    
    ops = {"+" : lambda x,y: x+y,
           "-" : lambda x,y: x-y,
           "*" : lambda x,y: x-y,}
    
    L = S.split(" ")

    stk = []
    
    for i in L:
        if i not in ops:
            stk.append(int(i))    
            print(stk)
        else:    
            print(stk,i)
            a = stk.pop()
            b = stk.pop()
            r = ops[i](a,b)
            stk.append(r)
            print(stk)


reverse_polish("2 3 73 + *")