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
        
        for k,v in transition.items():
            if k not in alphabet:
                raise ValueError(f"The transition table includes {k} which is not in the alphabet")
            if len(v) != states:
                raise ValueError(f"The transition row for {k} has the wrong number of states")
            if len(k) != 1:
                raise ValueError(f"The transition symbol {k} is too long")
        
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
    
    T = {"0": [1,0],
         "1": [0,1]
        }
    
    
    mynfa = NFA(2,"01",T,0,[0])
    
    
    for string in ["0001001011111"]:
        print(string,mynfa(string))
    
    print("\nWords from the language with up to five letters")
    print(mynfa.language(5))
    
    
    #          0 1 2 3 4
    T = {"M": [1,2,2,2,2],
         "m": [2,3,2,3,2],
         "R": [1,2,2,2,2],
         "r": [2,3,2,3,2],
         "S": [1,2,2,2,2],
         "s": [2,3,2,3,2],
         "D": [1,2,2,2,2],
         "d": [2,3,2,3,2],
         ".": [2,2,2,4,2],
        }
    
    
    mynfa2 = NFA(5,"MmRrSsDd.",T,0,[4])
    
    print("\nGenerate words from a language that looks like abbreviated titles")
    print(mynfa2.language(4))