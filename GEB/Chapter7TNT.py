import re
from Utils.StringManip import bracket_matching


class TNT:
    
    def __init__(self,s=""):
        self.s = s
        
    def EXISTS(self,a):
        if is_atom(str(a)):
            return TNT(f"∃{a}:{self.s}")
        else:
            raise Exception(f"Existential quantifier does not apply to {a}")
        
    def FOR_ALL(self,a):
        if is_atom(str(a)):
            return TNT(f"∀{a}:{self.s}")
        else:
            raise Exception(f"Universal quantifier does not apply to {a}")

    def AND(self,y):
        return TNT(f"<{self.s}∧{y}>")
        
    def OR(self,y):
        return TNT(f"<{self.s}∨{y}>")
        
    def IF(self,y):
        return TNT(f"<{self.s}⊃{y}>")
        
    def NOT(self,):
        return TNT(f"~{self.s}")
    
    def SUCC(self):
        if is_num(self.s):
            return TNT(f"S{self.s}")
        else:
            raise Exception(f"Cannot have successor of {self.s}")
      
        
    def ADD(self,y):
        return TNT(f"({self.s}+{y})")

    def MUL(self,y):
        return TNT(f"({self.s}⋅{y})")
    
    def EQ(self,y):
        return TNT(f"{self.s}={y}")
        
    def ASSERT(self,y):
        return TNT(f"{self.s}{y}")
        
    def __str__(self):
        return self.s

# ∧∨⊃∃∀⋅
def is_atom(x):
    if re.match("^[a-z]\'*$",x):
        return True
    return False

def is_num(x):
    while x[0] == "S":
        x = x[1:]
    if x == "0" or is_atom(x):
        return True
    return False



#def translate_TNT(s):
#    re.findall("")



if __name__ == '__main__':
    zero = TNT("0")
    one = zero.SUCC()
    two = one.SUCC()
    b = TNT("b")
    sq = b.MUL(b)
    ex_sq = sq.EXISTS(b)
    ex_sq_2 = ex_sq.EQ(two)
    not_ex_sq_2 = ex_sq_2.NOT()
    print(zero)
    print(one)
    print(two)
    print(b)
    print(sq)
    print(ex_sq)
    print(ex_sq_2)
    print(not_ex_sq_2)
    