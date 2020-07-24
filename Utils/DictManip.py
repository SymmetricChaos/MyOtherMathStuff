def sort_by_values(D):
    L = sorted(D.items(), key=lambda kv: kv[1])
    return L

def show_dict(D,superdict=""):
    """
    Recursively show the contents of a dictionary or iterable that may contain
    other dictionaries or iterables
    """
    if type(D) == dict:
        if len(D) == 0:
            print(f"{superdict}: {D}")
        for key,val in D.items():
            show_dict(val,superdict=f"{superdict}['{key}']")
    
    elif type(D) in (list,tuple):
        if len(D) == 0:
            print(f"{superdict}: {D}")
        for n,i in enumerate(D):
            show_dict(i,superdict=f"{superdict}[{n}]")
    
    else:
        print(f"{superdict}: {D}")