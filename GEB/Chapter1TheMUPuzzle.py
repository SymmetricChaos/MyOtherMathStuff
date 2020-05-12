def MIU_rule1(S):
    if S[-1] == "I":
        yield S + "U"


def MIU_rule2(S):
    if S[0] == "M":
        yield S + S[1:]

def MIU_rule3(S):
    for pos in range(len(S)):
        if S[pos:pos+3] == "III":
            yield S[:pos] + "U" + S[pos+3:]

def MIU_rule4(S):
    for pos in range(len(S)):
        if S[pos:pos+2] == "UU":
            yield S[:pos] + S[pos+2:]


def MUI_theorems(n):
    
    rules = [MIU_rule1,MIU_rule2,MIU_rule3,MIU_rule4]
    
    
    theorems_old = set(["MI"])
    theorems_new = set(["MI"])
    
    for i in range(n):
        for string in theorems_old:
            for rule in rules:
                for result in rule(string):
                    theorems_new.add(result)
        theorems_old = theorems_new.copy()
    
    print(theorems_new)




    
if __name__ == '__main__':
    MUI_theorems(3)
