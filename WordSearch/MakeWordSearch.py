from random import sample

class WordGrid:
    
    # Define number of rows and columns
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.grid = [" "]*(rows*cols) 
    
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
        word = frame["words"].pop()
        
        res = try_word(word,frame)
                
        if res == True:
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
            




def try_word(word,frame):
    gr = frame["grid"]
    p = pos
    
    while len(frame["positions"]) > 0:
        pos = frame["positions"].pop()
            
        while len(frame["directions"]) > 0:
            direct = frame["directions"].pop()
                
    
    for l in word:
        if gr.grid[p] == " ":
            gr.grid[p] = l
        elif  gr.grid[p] == l:
            pass
        else:
            return False
        loc = wordgrid.pos_to_pair(p)
        loc = [loc[0]+direction[0],loc[1]+direction[1]]
        p = wordgrid.pair_to_pos(loc[0],loc[1])
    return True
    

if __name__ == '__main__':
    G = WordGrid(10,10)
    print(G.grid)
    
    try_word("apple",55,(0,1),G)
    try_word("apple",66,(-1,1),G)
    
    G.show()
    
    print(sample([i for i in range(10)],10))