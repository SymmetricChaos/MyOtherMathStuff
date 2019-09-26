def rules(s):
    if s in ("111","100","000"):
        return "0"
    else:
        return "1"

def Rule110(S):
    out = "0"
    for i in range(len(S)-2):
        out += rules(S[i:i+3])
    out += rules(S[0]+S[-2]+S[-2])
    return out
    
S = "00000000000000000000000000000000000000000000001"
for i in range(45):
    print(S.replace("0"," "))
    S = Rule110(S)