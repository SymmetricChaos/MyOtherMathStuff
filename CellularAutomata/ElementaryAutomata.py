def cell_rule(n):
    """Higher order function functions for elementary cellular automata"""
    
    if n < 0:
        raise ValueError("Must be non-negative")
    if n > 255:
        raise ValueError("Must be less than 256")
    
    # Covert the number to the rule
    r = ["0","0","0","0","0","0","0","0"]
    for i in range(8):
        n,rem = divmod(n,2)
        r[i] = str(rem)
    r.reverse()
    
    patterns = ("111","110","101","100","011","010","001","000")
    
    zero = []
    
    for i,j in zip(r,patterns):
        if i == "0":
            zero.append(j)


    def rule(s):
        if s in zero:
            return "0"
        else:
            return "1"
        
    def apply_rule(S):
        out = rule("0"+S[0]+S[1])
        for i in range(len(S)-2):
            out += rule(S[i:i+3])
        out += rule(S[-2]+S[-1]+"0")
        return out
        
    return apply_rule