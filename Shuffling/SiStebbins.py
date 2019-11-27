rank = "A23456789TJQK"
suit = "♠♥♣♦"
D = []
for s in suit:
    for r in rank:
        D.append(r+s)

si_stebbins = []
pos = 0
for i in range(52):
    si_stebbins.append(D[pos])
    pos = (pos + 17) % 52
print(si_stebbins)