# Find cycles produced by an interated fuction

def floyds_algorithm(func,x):
    slow = func(x)
    fast = func(func(x))
    # Run until both slow and fast are inside the
    # cycle
    while fast != slow:
        slow = func(slow)
        fast = func(func(fast))



def f(n):
    D = {0:6, 1:6, 2:0, 3:1,
         4:4, 5:3, 6:3, 7:4,
         8:0}
    return D[n]

print(floyds_algorithm(f,0))