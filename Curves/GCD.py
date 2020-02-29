def egcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def gcd(*args):
    """Greatest Common Denominator"""

    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return gcd(*args[0])
    
    # the gcd of a single number is itself
    if len(args) == 1:
        return args[0]
    
    # calculate gcd for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        g,_,_ = egcd(a,b)
        return g
    
    # if more than two break it up recursively
    a = gcd(*args[0:2])
    b = gcd(*args[2:])
    return gcd(a,b)

	
def lcm(*args):
    """Least Common Multiple"""
    
    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return lcm(*args[0])
    
    # the lcm of a single number is itself
    if len(args) == 1:
        return args[0]
    
    # calculate lcm for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        g,_,_ = egcd(a,b)
        return abs(a*b)//g
    
    # if more than two break it up recursively
    a = lcm(*args[0:2])
    b = lcm(*args[2:])
    return lcm(a,b)