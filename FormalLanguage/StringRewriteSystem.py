from random import choice, choices, shuffle

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

    def apply(self,string,n=1):
        positions = []
        Plen = len(self.P)
        for i in range(0,len(string)-Plen+1):
            if string[i:i+Plen] == self.P:
                positions.append(i)
        pos = positions[n]
        return string[:pos] + self.R + string[pos+Plen:]



def random_AB_game(S,rules):
    for n,R in enumerate(rules,1):
        print(f"Rule {n}: {R}")
    
    oldS = ""
    while not S == oldS:
        print(S)
        oldS = S
        shuffle(rules)
        for R in rules:
            try:
                S = R.apply_random(S)
                break
            except:
                pass
                



if __name__ == '__main__':
    rule_set_1 = [rewrite_rule("AB","A"),
                  rewrite_rule("BA","A"),
                  rewrite_rule("AA","B"),
                  rewrite_rule("BB","B")
                 ]

    rule_set_2 = [rewrite_rule("AB","BBBA"),
                  rewrite_rule("BA","A"),
                  rewrite_rule("AA","BBBB"),
                  rewrite_rule("BB","B")
                 ]
    
    S = choices("AB",k=15)
    S = "".join(S)
    
    random_AB_game(S,rule_set_1)
    print()
    random_AB_game(S,rule_set_2)
    