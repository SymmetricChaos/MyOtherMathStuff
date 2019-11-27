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

print(multi_riffle(D,2))