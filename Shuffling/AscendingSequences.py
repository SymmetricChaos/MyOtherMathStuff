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
    from Shuffles import riffle, cut_deck, overhand, faro, fisher_yates
    
    D = [i for i in range(52)]
    
    print("A truly random sequence produces numerous short ascending sequences")
    L = fisher_yates(D)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    print("\n\n")
    
    
    
    print()
    print("\nA single riffle shiffle creates just two ascending sequences")
    L = riffle(D,1)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    
    print()
    print("\nRiffling twice is a bit better but clearly not random")
    L = riffle(D,2)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    
    print()
    print("\nAfter about 7 shuffles the results appear similar to a truly random arrangement")
    L = riffle(D,7)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    print("\n\n")
    
    
    
    print()
    print("\nThe overhand shuffle leaves at least one long sequence the first time")
    L = overhand(D,1)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    
    print()
    print("\nThe second overhand shuffle looks much better")
    L = overhand(D,2)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    
    print()
    print("\nAfter numerous overhand shuffles the result is not that much better")
    L = overhand(D,7)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    print("\n\n")
    
    
    print()
    print("\nThe faro shuffle, a 'perfect' riffle, is not in fact random at all")
    L = faro(D,1)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    print("\n\n")
    
    
    print()
    print("\nRepeatedly cutting the deck can never produce more than two ascending sequences.\nHere is the result of 50 cuts.")
    L = [i for i in range(20)]
    for i in range(50):
        L = cut_deck(L)
    print(L)
    print(len(ascending_sequences(L)),"sequences")
    