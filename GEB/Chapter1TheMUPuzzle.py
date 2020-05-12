import re

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

# We use regex to save some work here. It doesn't matter where in a string of
# U's we remove a UU. So we'll always remove it from the start.
def MIU_rule4(S):
    UU_pos = [i.span()[0] for i in re.finditer("UU+",S)]
    for pos in UU_pos:
        yield S[:pos] + S[pos+2:]


def MUI_theorems(n):
    
    rules = [MIU_rule1,MIU_rule2,MIU_rule3,MIU_rule4]
    
    
    theorems_old = set(["MI"])
    theorems_all = set(["MI"])
    
    for i in range(n):
        # We know no new theorems yet
        theorems_new = set([])
        # Go through every string/theorem we know
        for string in theorems_old:
            # For each rule we can apply
            for rule in rules:
                # For each possible result of that rule
                for result in rule(string):
                    # If we have never seen it before
                    if result not in theorems_all:
                        # Make it a new theorem
                        theorems_new.add(result)
                        theorems_all.add(result)
    
        # The theorems we've just found are now old
        theorems_old = theorems_new.copy()
        theorems_new = set([])
    
    return theorems_all




    
if __name__ == '__main__':
    T = MUI_theorems(5)
    print(sorted(T,key=len))
    
    