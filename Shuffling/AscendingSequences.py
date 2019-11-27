def ascending_sequences(L):
    L = L.copy()
    S = []
    
    while len(L) > 0:
        # Start with an empty list and the first element of the current list
        T = []
        s = [L.pop(0)]
        # Pop each element of the list, if it's the next in a sequence it goes
        # into the s list, otherwise the T list
        while len(L) > 0:
            a = L.pop(0)
            if a == s[-1]+1:
                s.append(a)
            else:
                T.append(a)
        # Add the sequence that was found to the list of sequences
        S.append(s)
        # The remainder is renamed to L to reuse
        L = T
        
    return S





if __name__ == '__main__':
    from random import sample
    from Shuffles import riffle, cut_deck
    
    print("\n\nA truly random sequence produces numerousc short ascending sequences")
    L = sample([i for i in range(20)],20)
    print(L)
    print(ascending_sequences(L))
    
    print()
    print("\n\nA single riffle shiffle creates just two ascending sequences")
    L = riffle([i for i in range(20)],1)
    print(L)
    print(ascending_sequences(L))
    
    print()
    print("\n\nRiffling twice is a bit better but clearly not random")
    L = riffle([i for i in range(20)],2)
    print(L)
    print(ascending_sequences(L))
    
    print()
    print("\n\nAfter about 7 shuffles the results appear similar to a truly random arrangement")
    L = riffle([i for i in range(20)],7)
    print(L)
    print(ascending_sequences(L))
    
    print()
    print("\n\nRepeatedly cutting the deck can never produce more than two ascending sequences.\nHere is the result of 50 cuts.")
    L = [i for i in range(20)]
    for i in range(50):
        L = cut_deck(L)
    print(L)
    print(ascending_sequences(L))