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

# Directions as increments
directions = ( (0,1),
               (1,1),
               (1,0),
               (-1,1),
               (0,-1),
               (-1,-1),
               (-1,0),
               (-1,1) )


#def build_word_search

def try_word(word,pos,direction,wordgrid):
    p = pos
    for l in word:
        if wordgrid.grid[p] == " ":
            wordgrid.grid[p] = l
        elif  wordgrid.grid[p] == l:
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
    try_word("apple",55,(-1,1),G)
    
    G.show()