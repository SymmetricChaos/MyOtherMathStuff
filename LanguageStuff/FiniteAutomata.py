# Non-Deterministic Finite Automata
# class NDFA

# Deterministic Finite Automata
class DFA:
    
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
                raise ValueError(f"The transition table include {k} which is not in the alphabet")
            if len(v) != states:
                raise ValueError(f"The transition row for {k} has the wrong number of states")
        
        if type(accept) == list:
            accept = set(accept)
        
        
        self.states = [i for i in range(states)]
        self.alphabet = alphabet
        self.transition = transition
        self.cur_state = start
        self.accept = accept
    
    def __call__(self,string):
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            self.cur_state = self.transition[symbol][self.cur_state]
        if self.cur_state in self.accept:
            return True
        return False

T = {"0": [1,0],
     "1": [0,1]
    }


mydfa = DFA(2,"01",T,0,[0])


for string in ["0001001011111"]:
    print(string,mydfa(string))