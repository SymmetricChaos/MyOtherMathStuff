from ElementaryAutomata import cell_rule


Rule_110 = cell_rule(110)

    
S = "00000000000000000000000000000000000000000000001"
for i in range(45):
    print(S.replace("0"," "))
    S = Rule_110(S)