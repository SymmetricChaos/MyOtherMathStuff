import random
import numpy as np
import matplotlib.pyplot as plt 

def ice_cream_parlor():
    
    rate = 1
    bucket_size = 20
    flavors = 10
    
    flavors_list = [bucket_size]*flavors
    
    ctr = 0
    while True:
        ctr += rate
        choice = random.randint(0,9)
        flavors_list[choice] -= 1
        if flavors_list[choice] == 0:
            break
        
    return ctr
    
L = []
for i in range(8000):
    L.append(ice_cream_parlor())
    

plt.hist(L,bins=10)
print(np.median(L))