import random
import numpy as np
import matplotlib.pyplot as plt 

def ice_cream_parlor(rate=1,bucket=20,flavors=10):
    
    # rate is minutes between customers
    # bucket is orders until bucket is empty
    # flavors is number of flavor options
    
    flavors_list = [bucket]*flavors
    
    ctr = 0
    while True:
        ctr += rate
        choice = random.randint(0,9)
        flavors_list[choice] -= 1
        if flavors_list[choice] == 0:
            break
        
    return ctr
    
L = []
for i in range(10000):
    L.append(ice_cream_parlor())
    

plt.hist(L,bins=np.linspace(0,200,20))
print(np.median(L)/60)