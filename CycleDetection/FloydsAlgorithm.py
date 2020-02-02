# Find cycles produced by an interated fuction

def floyds_algorithm(func,x):
    slow = func(x)
    fast = func(func(x))
    # Run until both slow and fast are inside the
    # cycle
    while fast != slow:
        slow = func(slow)
        fast = func(func(fast))
    
    # Find the position where the cycle begins
    # Reset slow to the starting point and leave
    # fast inside the cycle
    # Save this point for later as "start"
    pos = 0
    slow = x
    while fast != slow:
        slow = func(slow)
        fast = func(fast)
        pos += 1
    start = slow
    
    # Find the length of the shortest cycle
    # That is we want to get AB rather than ABAB
    length = 1
    fast = f(slow)
    while fast != slow:
        fast = func(fast)
        length += 1
    
    # Get the elements of the cycle
    cyc = []
    for i in range(length):
        cyc.append(start)
        start = func(start)

    return pos,length,cyc


def f(n):
    D = {0:12, 1:6, 2:0, 3:1,
         4:4, 5:3, 6:3, 7:4,
         8:0, 9:13, 10:12, 11:4,
         12:9, 13:14, 14:0}
    return D[n]

for start in range(15):
    
    P,L,C = floyds_algorithm(f,start)
    
    print(f"{start} --> {C}")
    iters = []
    for i in range(15):
        iters.append(start)
        start = f(start)
    
    print(*iters)
    
    print()