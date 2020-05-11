def ordinals():
    n = "{}"
    while True:
        yield n
        n = "{" + n[1:-1] + n + "}"





if __name__ == '__main__':
    
    
    print("We can define an ordinal as the set containing all the ordinals before it.")
    print("This can be done without reference to the idea of 'the ordinals before it' simply by defining a successor function that builds the next ordinal as the union of the given ordinal with the set that contains it.")
    print("This makes it possible to define an order on them so that a < b iff a is an element of b.")
    
    ords = []
    for n,o in enumerate(ordinals()):
        print(n,o)
        ords.append(o)
        if n > 4:
            break