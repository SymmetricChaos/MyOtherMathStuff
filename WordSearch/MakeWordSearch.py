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
    def coord_to_pos(self,row,col):
        return row*self.cols + col

    # Convert a position to coordinates
    def pos_to_coord(self,pos):
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
            return self.coord_to_pos(row,col)
    
    
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





# Utility function for turning friendly named directions into ordered pairs
def name_to_direct(name):
    S = {"east": (0,1),
         "south-east": (1,1),
         "south": (1,0),
         "south-west": (1,-1),
         "west": (0,-1),
         "north-west": (-1,1),
         "north": (-1,0)}
    return S[name]



def word_search(words,size,directions=[],filltype="alphabet"):
    
    if any([len(w) > size for w in words]):
        raise Exception(f"Words cannot have more than {size} letters")
    
    if directions == []:
        directions = [ "east",
                       "south-east",
                       "south",
                       "south-west",
                       "west",
                       "north-west",
                       "north" ]

    # Just use a standard alphabet to fill blank spaces
    if filltype == "alphabet":
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Use the words themselves as the alphabet so that false letters have the
    # same frequencies as true letters
    elif filltype == "bootstrap":
        alpha = ""
        for w in words:
            alpha += w
    # Use the words themselves as the alphabet so that false letters have the
    # same frequencies as true letters
    # Also get all the digraphs from the words so they can be placed in the grid
    # as well as even better fakes, digraphs cannot cause a puzzle to become
    # impossible because they can be placed over existing words
    # Note that digraphs are placed in front of the word since we remove words
    # from the list back to front
    # This is much faster than placing the digrams first since digrams
    # placement will never require backtracking, in the worst case they are just
    # placed to overlap with the word they come from
    elif filltype == "digram":
        alpha = ""
        digrams = []
        for w in words:
            alpha += w
            for d in range(len(w)-1):
                digrams += [w[d:d+2]]
        words = digrams+words


    # Recursively place words (and digrams if requested) into the grid
    G = place_all_words(words,size,directions)

    # Fill in all remaining spaces with the requested alphabet
    for i in range(len(G.grid)):
        if G.grid[i] == "_":
            G.grid[i] = sample(alpha,1)[0]
            
    return G





# Internal functions for building the word search
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
            res = try_word(w,p,name_to_direct(d),gr)
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
        loc = wordgrid.pos_to_coord(pos)
        loc = [loc[0]+direct[0],loc[1]+direct[1]]

        # Fail out if the position doesn't exist
        if loc[0] < 0 or loc[1] < 0:
            return False
        if loc[0] > wordgrid.rows-1 or loc[1] > wordgrid.cols-1:
            return False
        
        # Convert the coordinates back
        pos = wordgrid.coord_to_pos(loc[0],loc[1])

    # If nothing went wrong return the grid that was created
    return g





# Solve a word search created with the above
def check_all_words(words,wordgrid):
    directions = ( "east",
                   "south-east",
                   "south",
                   "south-west",
                   "west",
                   "north-west",
                   "north" )
    for word in words:
        for pos in range(wordgrid.rows*wordgrid.cols):
            for direct in directions:
                res = check_word(word,pos,direct,wordgrid)
                if res:
                    yield res


def check_word(word,pos,direct,wordgrid):
    
    d = name_to_direct(direct)
    orig_loc = wordgrid.pos_to_coord(pos) 
    
    for l in word:
        # If the space matches keep going otherwise fail out
        if wordgrid.grid[pos] == l:
            pass
        else:
            return False
        
        # Step in the direction
        loc = wordgrid.pos_to_coord(pos)
        loc = [loc[0]+d[0],loc[1]+d[1]]

        # Fail out if the position doesn't exist
        if loc[0] < 0 or loc[1] < 0:
            return False
        if loc[0] > wordgrid.rows-1 or loc[1] > wordgrid.cols-1:
            return False
        
        # Convert the coordinates back
        pos = wordgrid.coord_to_pos(loc[0],loc[1])

    # Th coordinates of orig_loc have one added to make them more readable
    return (word,(orig_loc[0]+1,orig_loc[1]+1),direct)





# Section to build the PDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer
from time import time 


def list_to_intervals(L,n):
    out = []
    row = []
    for pos,val in enumerate(L,1):
        row.append(val)
        if pos % n == 0:
            out.append(row)
            row = []
    if len(row) > 0:
        out.append(row)
    return out


def grid_to_pdf(G,words):

    t = time()
    doc = SimpleDocTemplate(f"WordSearch{t}.pdf", pagesize=letter)
    
    data = G.as_list()
    
    # container for the 'Flowable' objects
    elements = []
    
    wordsearch = Table(data,style=[("ALIGN", (0, 0), (-1, -1), "CENTER"),])
    space = Spacer(1, 30)
    wordlist = Table(list_to_intervals(words,3),style=[("BOX",(0,0),(-1,-1),2,colors.gray)])

    elements = [wordsearch,space,wordlist]

    # write the document to disk
    doc.build(elements)





if __name__ == '__main__':

    word_list = ["azalea","buttercup","carnation","daffodil",
                 "daisy","goldenrod","honeysuckle","jasmine","lavender",
                 "laurel","magnolia","marigold","narcissus","poinsettia",
                 "rhododendron","snapdragon","tulip","wisteria","zinnia"]
    
    word_list = [w.upper() for w in word_list]
    
    G = word_search(word_list,size=22,filltype="digram")
    print(str(G).upper())

    for i in check_all_words(word_list,G):
        print(i)
        
    grid_to_pdf(G,word_list)
    