from random import choice, shuffle

class rewrite_rule:
    
    def __init__(self,pattern,replacement):
        self.P = pattern
        self.R = replacement
    
    def __str__(self):
        return f"{self.P} 🡪 {self.R}"
    
    def apply_random(self,string):
        positions = []
        Plen = len(self.P)
        for i in range(0,len(string)-Plen+1):
            if string[i:i+Plen] == self.P:
                positions.append(i)
        pos = choice(positions)
        return string[:pos] + self.R + string[pos+Plen:]



def random_AB_game(S,rules,stopif):
    for n,R in enumerate(rules,1):
        print(f"Rule {n}: {R}")
    
    print(S)
    while not stopif(S):
        shuffle(rules)
        for R in rules:
            try:
                S = R.apply_random(S)
                break
            except:
                pass
                
        print(S)


if __name__ == '__main__':
    rule1 = rewrite_rule("AB","A")
    rule2 = rewrite_rule("BA","A")
    rule3 = rewrite_rule("AA","B")
    rule4 = rewrite_rule("BB","B")
    
    random_AB_game("ABABBBBABBAAAABA",[rule1,rule2,rule3,rule4],lambda x: len(x) == 1)
    
    print()
    rule1 = rewrite_rule("AB","BBBA")
    rule2 = rewrite_rule("BA","A")
    rule3 = rewrite_rule("AA","BBBB")
    rule4 = rewrite_rule("BB","B")
    
    random_AB_game("AAAAAAABAAAAAABA",[rule1,rule2,rule3,rule4],lambda x: len(x) == 1)