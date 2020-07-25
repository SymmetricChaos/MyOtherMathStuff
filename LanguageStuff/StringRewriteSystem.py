from random import choice, choices, shuffle

class rewrite_rule:
    
    def __init__(self,pattern,replacement):
        self.P = pattern
        self.R = replacement
    
    def __str__(self):
        return f"{self.P} 🡪 {self.R}"
    
    def apply_random(self,string):
        """Find a random place where the rules applies"""
        positions = []
        Plen = len(self.P)
        for i in range(0,len(string)-Plen+1):
            if string[i:i+Plen] == self.P:
                positions.append(i)
        
        if len(positions) == 0:
            raise Exception(f"{self.P} not in {string}")
        
        pos = choice(positions)
        return string[:pos] + self.R + string[pos+Plen:]
    
    def apply(self,string,n=0):
        """Apply to the nth occurence, defaults to leftmost"""
        ctr = 0
        Plen = len(self.P)
        for pos in range(0,len(string)-Plen+1):
            if string[pos:pos+Plen] == self.P:
                if ctr == n:
                    return string[:pos] + self.R + string[pos+Plen:]
                else:
                    ctr += 1
        
        raise Exception(f"{self.P} not in {string}")




def random_system(S,rules):
    
    """
    Takes a starting string S and some rules and then applies the rules in a 
    random order trying random positions until it is no longer possible
    """
    
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


def random_left_system(S,rules):
    
    """
    Takes a starting string S and some rules and then applies the rules in a 
    random order always act as far left as possible
    """
    
    for n,R in enumerate(rules,1):
        print(f"Rule {n}: {R}")
    
    oldS = ""
    while not S == oldS:
        print(S)
        oldS = S
        shuffle(rules)
        for R in rules:
            try:
                S = R.apply(S)
                break
            except:
                pass



def random_AB_game(k=15,rule_set=0):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    if rule_set == 0:
        rules = [rewrite_rule("AB","A"),
                 rewrite_rule("BA","A"),
                 rewrite_rule("AA","B"),
                 rewrite_rule("BB","B")]
    
    if rule_set == 1:
        rules = [rewrite_rule("AB","BBBA"),
                 rewrite_rule("BA","A"),
                 rewrite_rule("AA","BBBB"),
                 rewrite_rule("BB","B")]
    
    random_system(S,rules)


def random_improper():
    rules = [rewrite_rule("S",""),
             rewrite_rule("S","aSa"),
             rewrite_rule("S","bSb"),]
    
    random_system("S",rules)

def random_nesting():
    rules = [rewrite_rule("S","SS"),
             rewrite_rule("S","()"),
             rewrite_rule("S","(S)"),
             rewrite_rule("S","[]"),
             rewrite_rule("S","[S]"),]
    
    random_system("S",rules)


def random_CSG():
    rules = [rewrite_rule("S","aBC"),
             rewrite_rule("S","aSBC"),
             rewrite_rule("CB","CZ"),
             rewrite_rule("CZ","WZ"),
             rewrite_rule("WZ","WC"),
             rewrite_rule("WC","BC"),
             rewrite_rule("aB","ab"),
             rewrite_rule("bB","bb"),
             rewrite_rule("bC","bc"),
             rewrite_rule("cC","cc")]
    
    random_left_system("S",rules)

if __name__ == '__main__':

    
    random_AB_game(15,0)
    print()
    random_AB_game(15,1)
    print()
    random_improper()
    print()
    random_nesting()
    print()
    random_CSG()
    