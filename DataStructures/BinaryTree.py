L = [1,2,3,4,5,6,7,None,None,None,None,None,None,None,None]

for pos,i in enumerate(L,1):
    if i != None:
        print(f"The children of {i} are")
        print(L[pos*2-1])
        print(L[pos*2])
        print()

    