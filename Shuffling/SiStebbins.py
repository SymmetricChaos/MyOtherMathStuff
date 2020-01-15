# Construct the Si Stebbins stack
# The cards are in CHASED order and each card is of rank three greater
# than the one before it
rank = "A23456789TJQK"
suit = "♣♥♠♦"
si_deck = []

pos1 = 0
pos2 = 0
for i in range(52):
    si_deck.append(rank[pos1]+suit[pos2])
    pos1 = (pos1 + 3) % 13
    pos2 = (pos2 + 1) % 4
    
print(si_deck)
print(len(set(si_deck)))



# Alternative construction of a Si Stebbins type stack.

# Create a deck of cards already sorted
rank = "A23456789TJQK"
suit = "♣♥♠♦"
deck = []
for s in suit:
    for r in rank:
        deck.append(r+s)

si_deck = []
pos = 0
for i in range(52):
    si_deck.append(deck[pos])
    pos = (pos + 15) % 52
    
print(si_deck)
print(len(set(si_deck)))