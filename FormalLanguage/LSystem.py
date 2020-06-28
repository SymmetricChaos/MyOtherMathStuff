class rewrite_rule:
    
    def __init__(self,variable,replacement):
        if len(variable) != 1:
            raise Exception("L-System rules apply only to single symbols")
        self.variable = variable
        self.replacement = replacement
    
    def __str__(self):
        return f"{self.variable} 🡪 {self.replacement}"

    def __repr__(self):
        return f"{self.variable} 🡪 {self.replacement}"

    def __call__(self,string):
        if string == self.variable:
            return self.replacement
        else:
            raise Exception("Rule does not apply.")


class LSystem:
    
    def __init__(self,rules,alphabet):
        self.rules = rules
        self.alphabet = alphabet
        
        for r in self.rules:
            if r.variable not in alphabet:
                raise Exception(f"The rule {r} does not act on the alphabet {alphabet}")
            
    def _variables(self):
        V = []
        for r in self.rules:
            V.append(r.variable)
        return V
            
    def _constants(self):
        C = []
        V = self.variables
        for char in self.alphabet:
            if char not in V:
                C.append(char)
        return C
    
    def describe(self):
        V = self.variables
        C = self.constants
        print(self.alphabet)
        for n,R in enumerate(self.rules,1):
            print(f"Rule {n}: {R}")
        print(f"Variables: {' '.join(V)}")
        print(f"Constants: {' '.join(C)}")
        
        
    def __call__(self,string):
        out = []
        for char in string:
            for r in self.rules:
                try:
                    out.append(r(char))
                except:
                    continue
                
        return "".join(out)

    variables = property(_variables)
    constants = property(_constants)



if __name__ == '__main__':
    r1 = rewrite_rule("A","AB")
    r2 = rewrite_rule("B","A")
    L = LSystem([r1,r2],"AB")
    L.describe()
    S = "B"
    for i in range(10):
        print(S)
        S = L(S)
    
    
    print("\n\n\n")
    r1 = rewrite_rule("0","1[0]0")
    r2 = rewrite_rule("1","11")
    L = LSystem([r1,r2],"01[]")
    L.describe()
    S = "0"
    for i in range(5):
        print(S)
        S = L(S)
    
