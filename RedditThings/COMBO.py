def reddit_COMBO(tapped,untapped):
    total = tapped+untapped
    floating = 0
    
    if total > 7 and untapped > 0:
        return 0
    
    else:
        while True:
            floating += total
            tapped += 1
            untapped -= 1
            
            if floating >= 7:
                untapped += 1
                total += 1
                floating -= 7
            
            if untapped == 0 and floating < 7:
                return 7*(7-total)-floating
            
            if untapped > 0 and total > 7 and floating > 7:
                return 0


print(reddit_COMBO(5,1))