from Shuffles import riffle


rank = "A23456789TJQK"
suit = "♠♥♣♦"
D = []
for s in suit:
    for r in rank:
        D.append(r+s)

print(D)
print()
print(riffle(D,1))
print()

print(riffle(D,2))