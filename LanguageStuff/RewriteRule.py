from random import choice, sample

class PatternMissingError(Exception):
    
    def __init__(self,pattern,string):
        self.errtext = f"{pattern} not in {string}"
        super().__init__(self.errtext)


class rewrite_rule:
    
    def __init__(self,pattern,replacement):
        self.pattern = pattern
        self.replacement = replacement
    
    def __str__(self):
        if self.replacement == "":
            return f"{self.pattern} 🡪 ε"
        return f"{self.pattern} 🡪 {self.replacement}"
    
    def __repr__(self):
        return str(self)
    
    def apply(self,string,n=0):
        
        """Apply to the nth occurence of the pattern, defaults to leftmost, zero indexed"""
        
        ctr = 0
        Plen = len(self.pattern)
        for pos in range(0,len(string)-Plen+1):
            if string[pos:pos+Plen] == self.pattern:
                if ctr == n:
                    return string[:pos] + self.replacement + string[pos+Plen:]
                else:
                    ctr += 1
        
        raise PatternMissingError(self.pattern,string)
    
    def apply_random(self,string):
        
        """Find a random place where the rules applies"""
        
        positions = []
        Plen = len(self.pattern)
        for i in range(0,len(string)-Plen+1):
            if string[i:i+Plen] == self.pattern:
                positions.append(i)
        
        if len(positions) == 0:
            raise PatternMissingError(self.pattern,string)
        
        pos = choice(positions)
        return string[:pos] + self.replacement + string[pos+Plen:]
        
    def apply_each(self,string):
        
        """
        Return a generator with each valid application of the rule to the 
        string. If there are no valid applications the generator is empty.
        """
        
        Plen = len(self.pattern)
        for pos in range(0,len(string)-Plen+1):
            if string[pos:pos+Plen] == self.pattern:
                yield string[:pos] + self.replacement + string[pos+Plen:]
    
    def apply_all(self,string):
        
        """
        Go through the string left to right and apply the rule whenever the
        pattern is found. Returns an unchanged string if the pattern is not
        present.
        """
        
        Plen = len(self.pattern)
        Rlen = len(self.replacement)
        left = ""
        right = string
        while True:
            if len(right) < Plen:
                return left + right
            if right[:Plen] == self.pattern:
                left += self.replacement
                right = right[Rlen+1:]
            else:
                left += right[0]
                right = right[1:]





# Barebones system with only the ability to apply rules
class rewrite_system:
    
    def __init__(self,rules):
        
        self.rules = rules
    
    
    def __str__(self):
        out = []
        for n,R in enumerate(self.rules,1):
            out.append(f"Rule {n}: {R}")
        return "\n".join(out)
    
    
    def compact_rules(self):
        
        """
        Show rules using the | symbol for or cannot be the default because
        options for applying the rules in the order stored exist
        """
        
        compacts = {}
        for R in self.rules:
            if R.pattern in compacts:
                if R.replacement == "":
                    compacts[R.pattern] += " | ε"
                else:
                    compacts[R.pattern] += f" | {R.replacement}"
            else:
                if R.replacement == "":
                    compacts[R.pattern] += "ε"
                else:
                    compacts[R.pattern] = R.replacement
        
        out = []
        for k,v in compacts.items():
            out.append(f"{k} 🡪 {v}")
            
        return "\n".join(out)
    
    
    def apply_nth(self,string,n):
        
        """Apply the nth rule to the leftmost position"""
        
        try:
            return self.rules[n].apply(string)
        except PatternMissingError:
            pass
        return string
    
    
    def apply_random(self,string):
        
        """In a random order try each rule until one has a position that works"""
        
        shuff_rules = sample(self.rules,len(self.rules))
        for R in shuff_rules:
            try:
                return R.apply_random(string)
            except PatternMissingError:
                pass
        return string
    
    
    def apply_ordered(self,string):
        
        """Apply the rules sequentially until one works always choosing leftmost position"""
        
        for R in self.rules:
            try:
                return R.apply(string)
            except PatternMissingError:
                pass
        return string



# String Rewrite System aka Semi-Thue System aka Unrestricted Grammar
class SRS(rewrite_system):
    
    def __init__(self,rules,alphabet):
        for R in rules:
            for p in R.pattern:
                if p not in alphabet:
                    raise Exception(f"{R} uses symbols outside of the alphabet")
            for r in R.pattern:
                if r not in alphabet:
                    raise Exception(f"{R} uses symbols outside of the alphabet")
            if R.replacement == "":
                continue
        
        if type(alphabet) != str:
            raise TypeError("Alphabet must be a string")
        if "ε" in alphabet:
            raise ValueError("The symbol ε is reserved as a metasymbol meaning the empty string")
        
        self.alphabet = alphabet
        super().__init__(rules)



# Extended (Right) Regular Grammar
class XRG(rewrite_system):
    
    def __init__(self,rules,terminals,nonterminals):
        for R in rules:
            if R.pattern not in nonterminals:
                raise Exception(f"{R} is an invlaid rule for this Extended Regular Grammar")
            if R.replacement == "":
                continue
            if R.replacement[-1] not in terminals+nonterminals:
                raise Exception(f"{R} is an invlaid rule for this Extended Regular Grammar")
            for symbol in R.replacement[:-1]:
                if symbol not in terminals:
                    raise Exception(f"{R} is an invlaid rule for this Extended Regular Grammar")
        
        if type(terminals) != str:
            raise TypeError("Terminals must be a string")
        if type(terminals) != str:
            raise TypeError("Nonterminals must be a string")
        if "ε" in terminals+nonterminals:
            raise ValueError("The symbol ε is reserved as a metasymbol meaning the empty string")
        self.terminals = terminals
        self.nonterminals = nonterminals
        super().__init__(rules)



# Context Free Grammar
class CFG(rewrite_system):
    
    def __init__(self,rules,terminals,nonterminals):
        for R in rules:
            if len(R.pattern) != 1:
                raise Exception(f"{R} is an invlaid for for a Context Free Grammar")
            if R.pattern not in nonterminals:
                raise Exception(f"{R} is an invlaid for for this Context Free Grammar")
            for r in R.replacement:
                if r not in terminals+nonterminals:
                    raise Exception(f"{R} is an invlaid for for this Context Free Grammar")
        
        if type(terminals) != str:
            raise TypeError("Terminals must be a string")
        if type(terminals) != str:
            raise TypeError("Nonterminals must be a string")
        if "ε" in terminals+nonterminals:
            raise ValueError("The symbol ε is reserved as a metasymbol meaning the empty string")
        self.terminals = terminals
        self.nonterminals = nonterminals
        super().__init__(rules)



def random_system_example(S,system,show_intermediate=True,lim=0):
    
    """
    Takes a starting string S and some rules and then applies the rules in a 
    random order trying random positions until it is no longer possible
    """
    
    if not show_intermediate:
        print(S)
        
    lim = lim+1
    oldS = ""
    ctr = 1
    while not S == oldS:
        ctr += 1
        if show_intermediate:
            print(S)
        oldS = S
        S = system.apply_random(S)
        if ctr == lim:
            break
    
    if not show_intermediate:
        print(S)