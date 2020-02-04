from math import gcd

# Provides a factorization of the input
# Doen't guarantee a prime factorization
def factorize(n):
    
    F = []
    
    # Quickly check a few small factors
    for i in [2,3,5,7,11,13,17,19,23,29,
              31,37,41,43,47,52,59,61,67]:
        while n%i == 0:
            F.append(i)
            n = n//i
    
    # After doing that try Pollard's Rho algorithm
    if n > 4489:
        F += pollard_factorization(n)
    
    return sorted(F)
    

def pollard_factorization(n):
    
    L = []
    # Recursively try to factor using Pollard's Rho
    for i in [2,3,5,7,11,13,17,19]:
        
        x = pollard_factorization_inner(i,i,n)

        if x != n:
            L += pollard_factorization(x)
            L += pollard_factorization(n//x)
            return L
    
    return [n]
        

def pollard_factorization_inner(x,y,n):

    d = 1
    
    def func(x):
        return (x*x+1)%n
    
    while d == 1:
        print(x,y)
        x = func(x)
        y = func(func(y))
        d = gcd(abs(x-y),n)
    
    print("\n\n")
    return d


    
    
#print(factorize(69342538559014215))
    
print(pollard_factorization_inner(2,2,10403))