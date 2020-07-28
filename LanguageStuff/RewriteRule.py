from random import choice, choices, shuffle

class PatternMissingError(Exception):
    
    def __init__(self,pattern,string):
        self.errtext = f"{pattern} not in {string}"
        super().__init__(self.errtext)

class rewrite_rule:
    
    def __init__(self,pattern,replacement):
        self.P = pattern
        self.R = replacement
    
    def __str__(self):
        return f"{self.P} 🡪 {self.R}"
    
    def apply(self,string,n=0):
        
        """Apply to the nth occurence of the pattern, defaults to leftmost, zero indexed"""
        
        ctr = 0
        Plen = len(self.P)
        for pos in range(0,len(string)-Plen+1):
            if string[pos:pos+Plen] == self.P:
                if ctr == n:
                    return string[:pos] + self.R + string[pos+Plen:]
                else:
                    ctr += 1
        
        raise PatternMissingError(self.P,string)
    
    def apply_random(self,string):
        
        """Find a random place where the rules applies"""
        
        positions = []
        Plen = len(self.P)
        for i in range(0,len(string)-Plen+1):
            if string[i:i+Plen] == self.P:
                positions.append(i)
        
        if len(positions) == 0:
            raise PatternMissingError(self.P,string)
        
        pos = choice(positions)
        return string[:pos] + self.R + string[pos+Plen:]
        
    def apply_each(self,string):
        
        """
        Return a generator with each valid application of the rule to the 
        string. If there are no valid applications the generator is empty.
        """
        
        Plen = len(self.P)
        for pos in range(0,len(string)-Plen+1):
            if string[pos:pos+Plen] == self.P:
                yield string[:pos] + self.R + string[pos+Plen:]
    
    def apply_all(self,string):
        """
        Go through the string left to right and apply the rule whenever the
        pattern is found. Returns an unchanged string if the pattern is not
        present.
        """
        
        Plen = len(self.P)
        Rlen = len(self.R)
        left = ""
        right = string
        while True:
            if len(right) < Plen:
                return left + right
            if right[:Plen] == self.P:
                left += self.R
                right = right[Rlen+1:]
            else:
                left += right[0]
                right = right[1:]





def random_system(S,rules,show_intermediate=True,lim=0):
    
    """
    Takes a starting string S and some rules and then applies the rules in a 
    random order trying random positions until it is no longer possible
    """
    
    for n,R in enumerate(rules,1):
        print(f"Rule {n}: {R}")
    
    if not show_intermediate:
        print(S)
    
    oldS = ""
    ctr = 1
    while not S == oldS:
        ctr += 1
        if show_intermediate:
            print(S)
        oldS = S
        shuffle(rules) # Have to shuffle to that system always terminates
        for R in rules:
            try:
                S = R.apply_random(S)
                break
            except PatternMissingError:
                pass
        if ctr == lim:
            break
    if not show_intermediate:
        print(S)


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
            except PatternMissingError:
                pass