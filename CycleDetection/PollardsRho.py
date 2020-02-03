from math import gcd

def factorize(n):
    
    F = []
    
    # Quickly check a few small factors
    for i in [2,3,5,7,11,13,17,19,23,29,
              31,37,41,43,47,52,59,61,67]:
        while n%i == 0:
            F.append(i)
            n = n//i
    
    if n > 361:
        F += pollard_factorization(n)
    
    return sorted(F)
    

def pollard_factorization(n):
    
    L = []
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
        x = func(x)
        y = func(func(y))
        d = gcd(abs(x-y),n)
        
    return d


    
    
print(factorize(69342538559014215))