def show_dict(D):
    for i,j in D.items():
        print(f"{i}: {j}")
        
def sort_by_values(D):
    L = sorted(D.items(), key=lambda kv: kv[1])
    return L