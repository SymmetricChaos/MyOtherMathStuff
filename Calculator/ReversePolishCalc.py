from math import sqrt



def reverse_polish(S):
    assert type(S) == str
    
    operation = {"+" : lambda x,y: x+y,
                 "*" : lambda x,y: x*y,
                 "sqrt" : lambda x: sqrt(x),
                 "-" : lambda x,y: y-x,
                 "/" : lambda x,y: y/x
                }
    
    arity = {"+" : 2,
             "*" : 2,
             "sqrt" : 1,
             "-" : 2,
             "/" : 2
             }
    
    L = S.split(" ")

    stk = []
    
    for i in L:
        if i not in operation:
            stk.append(int(i))    
            print(stk)
        else:
            print(stk,i)
            args = []
            for a in range(arity[i]):
                args.append(stk.pop())
            r = operation[i](*args)
            stk.append(r)
            print(stk)
    
    return stk


reverse_polish("2 8 2 * 3 73 + + + sqrt")
print()
reverse_polish("15 3 /")
print()
reverse_polish("15 3 -")