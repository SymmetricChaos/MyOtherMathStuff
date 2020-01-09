class WordGrid:
    
    # Define number of rows and columns
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.grid = [""]*(rows*cols) 
    
    def index(self,row,col = None):
        return row*self.cols + col

    def at(self,pos):
        r = pos//self.cols
        c = pos%self.cols
        return (r,c)
    
    def copy(self):
        return WordGrid(self.rows,self.cols,self.grid.copy())


if __name__ == '__main__':
    G = WordGrid(10,10)
    print(G.grid)
    print(G.index(5,8))