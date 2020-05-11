def G(n):
    if n == 0:
        return 0
    else:
        return n-G(G(n-1))


def H(n):
    if n == 0:
        return 0
    else:
        return n-H(H(H(n-1)))


def F(n):
    if n == 0:
        return 1
    else:
        return n-F(M(n-1))
    
def M(n):
    if n == 0:
        return 0
    else:
        return n-M(F(n-1))


def Q(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Q(n-Q(n-1)) + Q(n-Q(n-2))





if __name__ == '__main__':
    
    #Recreate the graphs from the book
    
    print("Diagram G")
    for i in range(25):
        print(G(i),end=" ")
    
    print("\nDiagram H")
    for i in range(25):
        print(H(i),end=" ")
        
    print("\nDiagram Q")
    for i in range(1,25):
        print(Q(i),end=" ")
        
#    print("\nMarried Recursion")
#    for i in range(10):
#        print(M(i),end=" ")