def imag_print(n,c):
    if n == 0:
        return ""
    elif n == 1:
        out = ""
    elif n == -1:
        out = "-"
    else:
        out = str(n)
    return out + c

class q_i:
    
    def __init__(self,coef=1):
        self.coef = coef
        
    def __str__(self):
        return imag_print(self.coef,"i")
        
    def __mul__(self,other):
        pr = self.coef*other.coef
        if type(other) == q_i:
            return -pr
        if type(other) == q_j:
            return q_k(pr)
        if type(other) == q_k:
            return q_j(-pr)
        return q_i(pr)
        
class q_j:
    
    def __init__(self,coef=1):
        self.coef = coef
    
    def __str__(self):
        return imag_print(self.coef,"j")
    
    def __mul__(self,other):
        pr = self.coef*other.coef
        if type(other) == q_i:
            return q_k(-pr)
        if type(other) == q_j:
            return -pr
        if type(other) == q_k:
            return q_i(pr)
        return q_j(pr)
    
        
class q_k:
    
    def __init__(self,coef=1):
        self.coef = coef
        
    def __str__(self):
        return imag_print(self.coef,"k")
        
    def __mul__(self,other):
        pr = self.coef*other.coef
        if type(other) == q_i:
            return q_j(pr)
        if type(other) == q_j:
            return q_i(-pr)
        if type(other) == q_k:
            return -pr
        return q_k(pr)
    
        
class H:
    
    def __init__(self,coef=0,i=0,j=0,k=0):
        self.coef = coef
        self.i = q_i(i)
        self.j = q_j(j)
        self.k = q_k(k)
    
    def __str__(self):
        out = ""
        for co in [self.coef,self.i,self.j,self.k]:
            out += str(co) + "+"
        return out
    
    def __add__(self,other):
        return H(self.coef+other.coef,
                 self.i+other.i,
                 self.j+other.j,
                 self.k+other.k)

print(H(1,1,1,-1))