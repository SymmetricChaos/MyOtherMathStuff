from random import sample

class WordGrid:
    
    # Define number of rows and columns
    def __init__(self,rows,cols,grid=None):
        self.rows = rows
        self.cols = cols
        if grid:
            self.grid = grid
        else:
            self.grid = ["_"]*(rows*cols) 
    
    def pair_to_pos(self,row,col):
        return row*self.cols + col

    def pos_to_pair(self,pos):
        r = pos//self.cols
        c = pos%self.cols
        return [r,c]
    
    def copy(self):
        return WordGrid(self.rows,self.cols,self.grid.copy())

    def show(self):
        for n,g in enumerate(self.grid):
            print(g,end = "")
            if (n+1) % self.cols == 0:
                print()

def make_word_search(words,size):
    
    # Directions as increments
    directions = ( (0,1),
                   (1,1),
                   (1,0),
                   (-1,1),
                   (0,-1),
                   (-1,-1),
                   (-1,0),
                   (-1,1) )

    grid = WordGrid(size,size)

    initial = {"words" : words,
             "grid" : grid.copy(),
             "directions" : sample(directions,8),
             "positions" : sample([i for i in range(size*size)],size*size)
            }
    
    stack = []
    
    stack.append(initial)
    
    while True:
        frame = stack[-1]
        res = try_options(frame)
                
        if res == True:
            frame["words"].pop()
            if len(frame["words"]) == 0:
                return frame["grid"]
            new_frame = {"words" : frame["words"],
                         "grid" : grid.copy(),
                         "directions" : sample(directions,8),
                         "positions" : sample([i for i in range(size*size)],size*size)
                         }
            stack.append(new_frame)
        else:
            stack.pop()
        
        if len(stack) == 0:
            raise Exception("Cannot create this word search")


def try_options(frame):
    w = frame["words"][-1]

    ps = frame["positions"]
    ds = frame["directions"]
    gr = frame["grid"]
    
    while len(ps) > 0:
        p = ps.pop()
        while len(ds) > 0:
            d = ds.pop()
            res = try_word(w,p,d,gr)
            if res == True:
                return True
    
    return False
            


def try_word(word,pos,direct,wordgrid):
    
    gr = wordgrid.copy()
    p = pos
    
    for l in word:
        if gr.grid[p] == "_":
            gr.grid[p] = l
        elif  gr.grid[p] == l:
            pass
        else:
            return False
        
        loc = wordgrid.pos_to_pair(p)
        loc = [loc[0]+direct[0],loc[1]+direct[1]]
        print(loc)
        
        if loc[0] < 0 or loc[1] < 0:
            return False
        if loc[0] > gr.rows-1 or loc[1] > gr.cols-1:
            return False
        
        p = wordgrid.pair_to_pos(loc[0],loc[1])
        
    wordgrid = gr
        

    
#    wordgrid = gr
    return True
    

if __name__ == '__main__':
    G = WordGrid(10,10)
    
    try_word("apple",55,(0,1),G)
    try_word("apple",66,(-1,1),G)
    try_word("apple",0,(0,1),G)
    
    G.show()
    
    print(G.pos_to_pair(0))
    
#    
#    S = make_word_search(["apple","fruit","cherry"],10)
#    S.show()