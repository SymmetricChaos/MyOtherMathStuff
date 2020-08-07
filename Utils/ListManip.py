def all_from(A,B):
    """Are all elements of A elements of B?"""
    for i in A:
        if i not in B:
            return False
    return True


def any_from(A,B):
    """Are any elements of A elements of B?"""
    for i in A:
        if i in B:
            return True
    return False


def flatten(L):
    """Turn a list of iterables and non-iterables into a single list of their elements"""
    flat = []
    for sublist in L:
        try: 
            iter(sublist)
        except TypeError:
            flat.append(sublist)
        else:
            for item in sublist:
                flat.append(item)
    return flat


def equal_spacing(L,w,justify="right"):
    """Print a single string with the elements of the list spaced out"""
    s = ""
    if justify == "right" or justify == "r":
        for i in L:
            s += f"{i:>{w}}"
    elif justify == "left" or justify == "l":
        for i in L:
            s += f"{i:<{w}}"
    elif justify == "center" or justify == "c":
        for i in L:
            s += f"{i}".center(w," ")
    else:
        raise Exception("Justify must be left or right.")
    print(s)


def equal_spacing_grid(L,w,justify="right"):
    """Print a list of iterables into a grid"""
    for r in L:
        equal_spacing(r,w,justify)


def lists_to_tuples(*args):
    """Convert lists to a list of tuples"""
    L = []
    for i in zip(*args):
        L.append(i)
    return L


def tuples_to_lists(L):
    """Convert a list of tuples to lists"""
    out = []
    W = len(L[0])
    for w in range(W):
        out.append( [i[w] for i in L] )
    return out


def list_to_sum(L):
    """Turns a list into a summation"""
    S = " + ".join(str(elem) for elem in L)
    S = S.replace("+ -","- ")
    return S


def list_to_prod(L):
    """Turns a list into a product"""
    S = " × ".join(str(elem) for elem in L)
    return S


def list_to_infix(L,operator="+"):
    """Turns a list into a summation by some symbol"""
    S = f" {operator} ".join(str(elem) for elem in L)
    return S


def chunk_size(L,n):
    return [L[i * n:(i + 1) * n] for i in range((len(L) + n - 1) // n )]


def inds_where(L,val):
    """All indices of list L that equal val"""
    return [i for i in range(len(L)) if L[i] == val]


def first_where(L,val):
    """First index of list L that equals val"""
    for pos,l in enumerate(L):
        if l == val:
            return pos
    return None


def sort_by_nth(L,n,func=None):
    """Sort a list of lists by the nth element of each sublist"""
    if func == None:
        f = lambda x: x[n]
        return sorted(L,key=f)
    else:
        f = lambda x: func(x[n])
        return sorted(L,key=f)