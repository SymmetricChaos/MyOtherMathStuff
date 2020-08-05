from RewriteRule import rewrite_rule, CFG
from collections import namedtuple

class LL1_Parser:
    
    def __init__(self,CFG,table):
        self.table = table
        self.CFG = CFG
    
    def __call__(self,string):
        stack = ["$","S"]
        string += "$"
        read = 0
        
        while True:
            # print([i for i in reversed(stack)])
            
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





if __name__ == '__main__':
    rules = [rewrite_rule("S","F"),
             rewrite_rule("S","(S+F)"),
             rewrite_rule("F","a")]
    gram = CFG(rules,"()a+","SF")
    
    table = [[1, -1,0,-1],
             [-1,-1,2,-1]]
    
    P = LL1_Parser(gram,table)
    print(P("(a+a)"))
    