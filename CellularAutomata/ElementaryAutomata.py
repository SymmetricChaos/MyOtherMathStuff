def cell_rule(r):
    """Higher order function to create a 1-dimensional cellular automata"""
    
    assert len(r) == 8
    patterns = ("111","110","101","100","011","010","001","000")
    
    zero = []
    
    for i,j in zip(r,patterns):
        if i == "0":
            zero.append(j)

    print(f"Creating rule {r} giving output 0 for:\n{zero}")
    
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