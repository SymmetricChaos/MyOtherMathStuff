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
    
    # Return what is at a given position
    # If it is out of bounds return # to indicate that    
    def at_pos(self,pos):
        if pos > len(self.grid):
            return "#"
        else:
            return self.grid[pos]
    
    # Return what is at a given coordinates
    # If it is out of bounds return # to indicate that
    def at_coord(self,row,col):
        if row > self.rows or col > self.cols:
            return "#"
        else:
            return self.pair_to_pos(row,col)
        
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
    
    def as_list(self):
        L = []
        ctr = 0
        for r in range(self.rows):
            new_row = []
            for c in range(self.cols):
                new_row.append(self.grid[ctr].upper())
                ctr += 1
            L.append(new_row)
        return L





# Utility function
def name_to_direct(name):
    S = {"east": (0,1),
         "south-east": (1,1),
         "south": (1,0),
         "south-west": (1,-1),
         "west": (0,-1),
         "north-west": (-1,1),
         "north": (-1,0)}
    return S[name]





# Crate a kids-style crossword with no particular symmetry
def make_crossword(words,size):
    
    if any([len(w) > size for w in words]):
        raise Exception(f"Words cannot have more than {size} letters")
    
    # Directons
    directions = ( "east",
                   "south" )
    
    # Recursively place words into the grid
    G = place_all_words(words,size,directions)

            
    return G




# Internal functions for building the crossword
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
        
        # If we've backtracked all the way then its not possible
        if len(stack) == 0:
            raise Exception("Cannot create this word search")
        
        elif len(stack) == 1:
            res = try_first_options(frame)
            
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
        else:  
        
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
        

def try_first_options(frame):
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
            res = try_first_word(w,p,name_to_direct(d),gr)
            if res:
                return res
    
    return False


def try_first_word(word,pos,direct,wordgrid):
    
    # Copy the grid in case the word can't be placed
    g = wordgrid.grid.copy()
    
    for l in word:
        g[pos] = l
        
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
            res = try_word(w,p,name_to_direct(d),gr)
            if res:
                return res
    
    return False


# Word needs to start at an existing letter
# Word cannot have other letters in the cross positions
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
    
        if direct == "east":
    
            # Step in the direction
            loc = wordgrid.pos_to_pair(pos)
            loc = [loc[0],loc[1]+1]
    
            # Fail out if the position doesn't exist
            if loc[0] < 0 or loc[1] < 0:
                return False
            if loc[0] > wordgrid.rows-1 or loc[1] > wordgrid.cols-1:
                return False
            
            # Fail out if another letter is above, below, or right
            if wordgrid.at_coords(loc[0]+1,loc[1]) not in "_#":
                return False
            if wordgrid.at_coords(loc[0]-1,loc[1]) not in "_#":
                return False
            if wordgrid.at_coords(loc[0],loc[1]+1) not in "_#":
                return False
            
            # Convert the coordinates back
            pos = wordgrid.pair_to_pos(loc[0],loc[1])
        
        if direct == "south":
            
            # Step in the direction
            loc = wordgrid.pos_to_pair(pos)
            loc = [loc[0]+1,loc[1]]
    
            # Fail out if the position doesn't exist
            if loc[0] < 0 or loc[1] < 0:
                return False
            if loc[0] > wordgrid.rows-1 or loc[1] > wordgrid.cols-1:
                return False
            
            # Fail out if another letter is above, below, or right
            if wordgrid.at_coords(loc[0],loc[1]+1) not in "_#":
                return False
            if wordgrid.at_coords(loc[0],loc[1]-1) not in "_#":
                return False
            if wordgrid.at_coords(loc[0]+1,loc[1]) not in "_#":
                return False

            # Convert the coordinates back
            pos = wordgrid.pair_to_pos(loc[0],loc[1])

    # If nothing went wrong return the grid that was created
    return g







if __name__ == '__main__':

    word_list = ["azalea","bouquet","buttercup","carnation","daffodil",
                 "daisy"]
    
    n = 17
    G = make_crossword(word_list,n)
    print(G)
