def cell_rule(r):
    """Higher order function to create a 1-dimensional cellular automata"""
    
    assert len(r) == 8
    R = ("111","110","101","100","011","010","001","000")
    
    zero = []
    
    for i,j in zip(r,R):
        if i == "0":
            zero.append(j)

    print(f"Creating rule {r} giving output 0 for:\n{zero}")
    
    def rule(s):
        if s in zero:
            return "0"
        else:
            return "1"
        
    def apply_rule(S):
        out = "0"
        for i in range(len(S)-2):
            out += rule(S[i:i+3])
        out += rule(S[0]+S[-2]+S[-2])
        return out
        
    return apply_rule



Rule110 = cell_rule("01101110")
S = "00000000000000000000000000000000000000000000001"
for i in range(45):
    print(S.replace("0"," "))
    S = Rule110(S)