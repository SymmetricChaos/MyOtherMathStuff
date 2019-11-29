def card_sequences(L):
    L1 = L.copy()
    S1 = []
    
    while len(L1) > 0:
        # Start with an empty list and the first element of the current list
        T = []
        s = [L1.pop(0)]
        # Pop each element of the list, if it's the next in a sequence it goes
        # into the s list, otherwise the T list
        while len(L1) > 0:
            a = L1.pop(0)
            if a == s[-1]+1:
                s.append(a)
            else:
                T.append(a)
        # Add the sequence that was found to the list of sequences
        S1.append(s)
        # The remainder is renamed to L to reuse
        L1 = T
        
    print(len(S1),"up sequences")

    return S1




if __name__ == '__main__':
    from Shuffles import riffle, cut_deck, overhand, faro, fisher_yates, mongean, pile_shuffle
    
    D = [i for i in range(52)]
    
    print("A truly random sequence produces numerous short ascending sequences")
    L = fisher_yates(D)
    print(L)
    card_sequences(L)
    print("\n\n")
    
    
    
    print("\n\nA single riffle shiffle creates just two ascending sequences")
    L = riffle(D,1)
    print(L)
    card_sequences(L)
    
    print("\n\nRiffling twice is a bit better but clearly not random")
    L = riffle(D,2)
    print(L)
    card_sequences(L)
    
    print("\n\nAfter seven shuffles the results appear similar to a truly random arrangement, as many as ten may be needed to guarantee a good shuffle")
    L = riffle(D,7)
    print(L)
    card_sequences(L)
    print("\n\n")
    
    
    
    print("\n\nThe overhand shuffle leaves at least one long sequence the first time")
    L = overhand(D,1)
    print(L)
    card_sequences(L)
    
    print("\n\nThe second overhand shuffle looks much better")
    L = overhand(D,2)
    print(L)
    card_sequences(L)
    
    print("\n\nAfter seven overhand shuffles the result is similar to riffle shuffling")
    L = overhand(D,7)
    print(L)
    card_sequences(L)
    print("\n\n")
    
    
    print("\n\nThe faro shuffle, a 'perfect' riffle, is not in fact random at all")
    L = faro(D,1)
    print(L)
    card_sequences(L)
    
    print("\n\nThe number of sequences doubles each time. Here is two faro shuffles.")
    L = faro(D,2)
    print(L)
    card_sequences(L)
    print("\n\n")
    
    
    print("\n\nThe Mongean shuffle is another nonrandom sort of shuffle. Unlike the Faro it produces lots of short sequences")
    L = mongean(D,1)
    print(L)
    card_sequences(L)
    
    print("\n\nIt only takes a few Mongean shuffles to produce a pattern that looks random although it is not")
    L = mongean(D,3)
    print(L)
    card_sequences(L)
    print("\n\n")
    
    
    
    print("\n\nA pile shuffle is generally regarded as a poor quality shuffle but it does effectively break up patterns")
    L = pile_shuffle(D,5)
    print(L)
    card_sequences(L)
    print("\n\n")
    
    
    
    print("\n\nRepeatedly cutting the deck can never produce more than two ascending sequences.\nHere is the result of 50 cuts.")
    L = D.copy()
    for i in range(50):
        L = cut_deck(L)
    print(L)
    card_sequences(L)
    