# Nondeterministic Finite Automata
class NFA:
    
    def __init__(self,states,alphabet,transition,start,accept):
        
        if type(states) != int:
            raise TypeError("State must be an integer number of states")
        if type(alphabet) != str:
            raise TypeError("Alphabet must be a string containing every symbol used")
        if type(transition) != dict:
            raise TypeError("Transition must be a dictionary")
        if type(start) != int:
            raise TypeError("Start must be the integer state that the DFA begins at")
        if type(accept) not in (list,set):
            raise TypeError("Accept must be a list or a set")
        
        lengths = set([])
        for k,v in transition.items():
            lengths.add(len(v))
            if k not in alphabet:
                raise ValueError(f"The transition table includes {k} which is not in the alphabet")
            if len(v) != states:
                raise ValueError(f"The transition row for {k} has the wrong number of states")
            if len(k) != 1:
                raise ValueError(f"The transition symbol {k} is too long")
            for s in v:
                if s > states-1:
                    raise ValueError(f"Transition on symbol {k} involves state {s} which does not exist")
            if k not in alphabet:
                raise ValueError(f"The symbol {k} has a transition but is not in the alphabet")
        
        if len(lengths) != 1:
            raise Exception("All rows of the transition table must be the same length")
        
        for symbol in alphabet:
            if symbol not in transition:
                raise ValueError(f"The symbol {symbol} has no associated transition")
        
        if type(accept) == list:
            accept = set(accept)
        
        self.states = [i for i in range(states)]
        self.alphabet = alphabet
        self.transition = transition
        self.start = start
        self.accept = accept
    
    
    def __call__(self,string):
        cur_state = self.start
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            cur_state = self.transition[symbol][cur_state]
        if cur_state in self.accept:
            return True
        return False
    
    
    def language(self,length=1):
        
        def NFA_language(NFA,cur_state,string,depth):
            if cur_state in NFA.accept:
                L = [string]
            else:
                L = []
            
            if len(string) == depth:
                return L
            
            for symbol,state in NFA.transition.items():
                L += NFA_language(NFA,state[cur_state],string+symbol,depth)
            
            return L
        
        return NFA_language(self,self.start,"",length)





if __name__ == '__main__':
    
    T1 = {"0": [1,0],
         "1": [0,1]
        }
    
    mynfa1 = NFA(2,"01",T1,0,[0])
    
    for string in ["0001001011111"]:
        print(string,mynfa1(string))
    
    print("\nBitstrings with an even number of zeroes. (Up to five characters)")
    print(mynfa1.language(5))
    
    # Make the failure state the last state
    #          0 1 2 3 4
    T2 = {"M": [1,4,4,4,4],
         "R": [1,4,4,4,4],
         "D": [1,4,4,4,4],
         "S": [1,4,4,4,4],
         "r": [4,2,2,4,4],
         "s": [4,2,2,4,4],
         ".": [4,4,3,4,4],
        }
    
    print("\nWords in the style of title abbreviations.")
    mynfa2 = NFA(5,"MRSDrs.",T2,0,[3])
    
    for string in ["Mr.","Dr.","Mrs.","Sr.","Xx."]:
        print(string,mynfa2(string))
    
    print("\nGenerate words up to four characters.")
    print(mynfa2.language(4))
    
    
    print("\nBOO with at least two and not more than 5 Os")
    #          0 1 2 3 4 5 6
    T3 = {"B": [1,7,7,7,7,7,7,7],
         "O": [6,2,3,4,5,6,7,7]
        }
    
    mynfa3 = NFA(8,"BO",T3,0,[3,4,5])
    
    print([i for i in mynfa3.language(7)])