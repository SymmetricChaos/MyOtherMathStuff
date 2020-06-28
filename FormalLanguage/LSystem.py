from random import choice

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



class random_rewrite_rule:
    
    def __init__(self,variable,replacements,probs):
        if len(variable) != 1:
            raise Exception("L-System rules apply only to single symbols")
        if len(replacements) != len(probs):
            raise Exception("replacements and probs must have the same length")
        self.variable = variable
        self.replacements = replacements
        self.probs = probs

    
#    def __str__(self):
#        return f"{self.variable} 🡪 {self.replacement}"
#
#
#    def __repr__(self):
#        return f"{self.variable} 🡪 {self.replacement}"


    def __call__(self,string):
        if string == self.variable:
            return choice(self.replacement,self.probs)
        else:
            raise Exception("Rule does not apply.")



class LSystem:
    
    def __init__(self,rules,alphabet):
        self.rules = rules
        self.alphabet = alphabet
        
        for r in self.rules:
            if r.variable not in alphabet:
                raise Exception(f"The rule {r} does not act on the alphabet {alphabet}")
        
        self.variables = [r.variable for r in self.rules]
        self.constants = [a for a in alphabet if a not in self.variables]
    

    def describe(self):
        V = self.variables
        C = self.constants
        print(f"Variables: {' '.join(V)}")
        print(f"Constants: {' '.join(C)}")
        for n,R in enumerate(self.rules,1):
            print(f"Rule {n}: {R}")


    def __call__(self,string):
        out = []
        for char in string:
            if char in self.constants:
                out.append(char)
            else:
                for r in self.rules:
                    try:
                        out.append(r(char))
                        break
                    except:
                        continue
                    
        return "".join(out)



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


    print("\n\n\n")
    r1 = rewrite_rule("X","X+YF+")
    r2 = rewrite_rule("Y","-FX-Y")
    L = LSystem([r1,r2],"XYF+-")
    L.describe()
    S = "FX"
    for i in range(4):
        print(S)
        S = L(S)
    