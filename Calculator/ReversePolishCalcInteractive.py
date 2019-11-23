from math import sqrt

def reverse_polish_interactive():

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
    

    L = []
    while True:
        S = input("Input: ")
        
        L += S.split(" ")
        
        stk = []
        
        for i in L:
            if i == "=":
                return stk
            elif i not in operation:
                stk.append(int(i))
            else:
                print(stk,i)
                args = []
                for a in range(arity[i]):
                    args.append(stk.pop())
                r = operation[i](*args)
                stk.append(r)
        L = stk
        print("\nCurrent Stack")
        print(L)

print(reverse_polish_interactive())