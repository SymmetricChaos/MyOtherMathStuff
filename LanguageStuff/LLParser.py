from RewriteRule import rewrite_rule, CFG


class LL1_Parser:
    
    def __init__(self,CFG,table):
        self.table = table
        self.CFG = CFG
    
    
    @property
    def pretty_table(self):
        
        spaced_terms = " ".join(self.CFG.terminals)
        out = f"  {spaced_terms}"
        
        for n,non in enumerate(self.CFG.nonterminals):
            s = non
            for i in table[n]:
                if i == -1:
                    s += " -"
                else:
                    s += f" {i}"
            out += f"\n{s}"
            
        return out


    def __call__(self,string):
        
        if "$" in string:
            raise ValueError("TIn this parser $ is reserved as a metasymbol")
        
        stack = ["$","S"]
        string += "$"
        read = 0
        
        while True:
            try:
                # print(string[:read+1],[i for i in reversed(stack)])
                
                if stack[-1] == "$":
                    if string[read] == "$":
                        return True
                    return False
                
                if stack[-1] == string[read]:
                    read += 1
                    stack.pop()
                    continue
                
                row = self.CFG.nonterminals.index(stack[-1])
                col = self.CFG.terminals.index(string[read])
                
                rule_num = table[row][col]
                rule = self.CFG.rules[rule_num]
                stack.pop()
                
                for i in reversed(rule.replacement):
                    stack.append(i)
            except ValueError:
                return False


# Computing the table
# def first_sets()




if __name__ == '__main__':
    rules = [rewrite_rule("S","F"),
             rewrite_rule("S","(S+F)"),
             rewrite_rule("F","a")]
    
    gram = CFG(rules,"()a+","SF")
    
    table = [[1, -1,0,-1],
             [-1,-1,2,-1]]
    
    P = LL1_Parser(gram,table)
    print(P.pretty_table)
    print()
    print(P("(a+a)"))

