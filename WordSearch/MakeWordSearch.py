from random import sample

class WordGrid:
    
    # Define number of rows and columns
    # Also create or accept a grid
    def __init__(self,rows,cols,grid=None):
        self.rows = rows
        self.cols = cols
        if grid:
            self.grid = grid
        else:
            self.grid = ["_"]*(rows*cols) 
    
    # Convert coordinates to a position
    def pair_to_pos(self,row,col):
        return row*self.cols + col

    # Convert a position to coordinates
    def pos_to_pair(self,pos):
        r = pos//self.cols
        c = pos%self.cols
        return [r,c]
    
    # Copy the whole object
    def copy(self):
        return WordGrid(self.rows,self.cols,self.grid.copy())

    # A simple string representation
    def __str__(self):
        S = ""
        for n,g in enumerate(self.grid):
            S += f"{g} "
            if (n+1) % self.cols == 0:
                S += "\n"
        return S





# Words written in readable directions
# Uniformly random filling
def easy_word_search(words,size):
    
    if any([len(w) > size for w in words]):
        raise Exception(f"Words cannot have more than {size} letters")
    
    # Directons as increments
    directions = ( (0,1),
                   (1,1),
                   (1,0) )
    
    # Recursively place words into the grid
    G = place_all_words(words,size,directions)

    # Fill empty spaces
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(G.grid)):
        if G.grid[i] == "_":
            G.grid[i] = sample(alpha,1)[0]
            
    return str(G)


# Words written in every direction
# Uniformly random filling
def medium_word_search(words,size):
    
    if any([len(w) > size for w in words]):
        raise Exception(f"Words cannot have more than {size} letters")
    
    # Directons as increments
    directions = ( (0,1),
                   (1,1),
                   (1,0),
                   (1,-1),
                   (0,-1),
                   (-1,-1),
                   (-1,0),
                   (-1,1) )

    # Recursively place words into the grid
    G = place_all_words(words,size,directions)

    # add random letters to empty spaces
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(G.grid)):
        if G.grid[i] == "_":
            G.grid[i] = sample(alpha,1)[0]
            
    return str(G)


# Words written in every direction
# Bootstrapping filling
def hard_word_search(words,size):
    
    if any([len(w) > size for w in words]):
        raise Exception(f"Words cannot have more than {size} letters")
    
    # Directons as increments
    directions = ( (0,1),
                   (1,1),
                   (1,0),
                   (1,-1),
                   (0,-1),
                   (-1,-1),
                   (-1,0),
                   (-1,1) )

    # Create alphabet from the words so that fake letter frequency is about the
    # same as true letter frequency
    # Also get all the digraphs from the words so they can be placed in the grid
    # as well as even better fakes, digraphs cannot cause a puzzle to become
    # impossible
    alpha = ""
    digraphs = []
    for w in words:
        alpha += w
        for d in range(len(w)-1):
            digraphs += [w[d:d+2]]

    # Recursively place words into the grid
    # Note that digraphs are placed in front of the word since we remove words
    # from back to front
    # This is much faster than placing the digraphs first since digraph
    # placement will never require backtracking, in the worst case they are just
    # placed to overlap with the word they come from
    G = place_all_words(digraphs+words,size,directions)

    for i in range(len(G.grid)):
        if G.grid[i] == "_":
            G.grid[i] = sample(alpha,1)[0]
            
    return str(G)


def place_all_words(words,size,directions):
    
    # Build a square grid
    grid = WordGrid(size,size)

    # First stack frame
    # Have to make sure everything is copied so we don't overwrite
    # other frames
    initial = {"words" : words.copy(),
               "grid" : grid.copy(),
               "directions" : sample(directions,len(directions)),
               "positions" : sample([i for i in range(size*size)],size*size)
               }
    stack = [initial]
    
    
    while True:
        
        # Use the top frame of the stack
        frame = stack[-1]
        res = try_options(frame)
        
        # If that gives a grid
        if res:
            # Accept the new grid and remove the word that was placed
            frame["grid"].grid = res
            frame["words"].pop()
            
            # If we're now out of words return the grid
            if len(frame["words"]) == 0:
                return frame["grid"]
            
            # Otherwise create a new stack frame
            new_frame = {"words" : frame["words"].copy(),
                         "grid" : frame["grid"].copy(),
                         "directions" : sample(directions,len(directions)),
                         "positions" : sample([i for i in range(size*size)],size*size)
                         }
            stack.append(new_frame)

        # If it gives back False then backtrack
        else:
            stack.pop()
        
        # If we've backtracked all the way then its not possible
        if len(stack) == 0:
            raise Exception("Cannot create this word search")
        

def try_options(frame):
    # Short names
    w = frame["words"][-1]
    ps = frame["positions"]
    ds = frame["directions"]
    gr = frame["grid"]
    
    # Eliminate positions one by one since they will not be reused
    # But we do not eliminate directions, they're reused in each position
    while len(ps) > 0:
        p = ps.pop()
        for d in ds:
            res = try_word(w,p,d,gr)
            if res:
                return res
    
    return False
            

def try_word(word,pos,direct,wordgrid):
    
    # Copy the grid in case the word can't be placed
    g = wordgrid.grid.copy()
    
    for l in word:
        # If the space is blank or matches write it
        # Otherwise fail out
        if g[pos] == "_":
            g[pos] = l
        elif g[pos] == l:
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

    # If nothing went wrong return the grid that was created
    return g
            

def child_safe_check(wordgrid):
    badwords = ["bitch","crap","cunt","damn","fuck","shit","slut","twat",
                "fag","dick","cock","pussy","piss","kill","rape"]
    
    directions = ( (0,1),
                   (1,1),
                   (1,0) )
    
    frame = {"words" :badwords,
             "grid" : grid.copy(),
             "directions" : directions,
             "positions" : [i for i in range(size*size)])
            }
    
    for w in badwords:
        try_options(frame)





if __name__ == '__main__':

    word_list = ["azalea","bouquet","buttercup","carnation","daffodil",
                 "daisy","goldenrod","honeysuckle","jasmine","lavender",
                 "laurel","magnolia","marigold","narcissus","poinsettia",
                 "rhododendron","snapdragon","tulip","wisteria","zinnia"]
    
    n = 20
    G = easy_word_search(word_list,n)
    print(G.upper())

    G = medium_word_search(word_list,n)
    print(G.upper())

    G = hard_word_search(word_list,n)
    print(G.upper())