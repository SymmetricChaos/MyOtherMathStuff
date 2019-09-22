from RiffleShuffle import multi_riffle


rank = "A23456789TJQK"
suit = "♠♥♣♦"
D = []
for s in suit:
    for r in rank:
        D.append(r+s)

print(D)
print()
print(multi_riffle(D,1))

print()

si_stebbins = []
pos = 0
for i in range(52):
    si_stebbins.append(D[pos])
    pos = (pos + 17) % 52
print(si_stebbins)