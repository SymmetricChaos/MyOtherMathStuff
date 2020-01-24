

def check_all_words(words,size,directions,wordgrid):
        
    for word in words:
        for pos in len(size*size):
            for direct in directions:
                res = check_word(word,pos,direct,wordgrid)
                if res:
                    yield res

def check_word(word,pos,direct,wordgrid):
    
    for l in word:
        # If the space matches keep going otherwise fail out
        if wordgrid[pos] == l:
            pass
        else:
            return False
        
        # Step in the direction
        loc = wordgrid.pos_to_pair(pos)
        loc = [loc[0]+direct[0],loc[1]+direct[1]]

        # Fail out if the position doesn't exist
        if loc[0] < 0 or loc[1] < 0:
            return False
        if loc[0] > wordgrid.rows-1 or loc[1] > wordgrid.cols-1:
            return False
        
        # Convert the coordinates back
        pos = wordgrid.pair_to_pos(loc[0],loc[1])

    return (word,pos,direct)
            

