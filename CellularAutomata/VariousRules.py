from ElementaryAutomata import cell_rule
from random import randint

for i in range(3):
    rule_number = randint(0,256)
    Rule = cell_rule(rule_number)
    
    print(f"\n\nRule {rule_number}\n")
    
    w = 20
    S = "0"*w + "1" + "0"*w
    for i in range(w):
        print(S.replace("0"," "))
        S = Rule(S)
