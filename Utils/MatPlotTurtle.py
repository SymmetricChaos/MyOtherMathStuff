import Utils.Drawing as Drawing
import math

class mplTurtle:
    
    def __init__(self,pos=(0,0),angle=0,draw=True,ax=None):
        self.pos = pos
        self.angle = angle%360
        self.draw = draw
        self.ax = ax
        
    def left(self,n):
        self.angle = (self.angle+n)%360
        
    def right(self,n):
        self.angle = (self.angle-n)%360
        
    def pen_up(self):
        self.draw = False
    
    def pen_down(self):
        self.draw = True
        
    def move_to(self,pos):
        if self.draw:
            Drawing.connect_p(self.pos,pos,self.ax)
        else:
            self.pos = pos
        
    def forward(self,n):
        a = math.radians(self.angle)
        h = math.sin(a)*n
        w = math.cos(a)*n
        newpos = (self.pos[0]+h,self.pos[1]+w)
        Drawing.connect_p(self.pos,newpos,self.ax)
        self.pos = newpos