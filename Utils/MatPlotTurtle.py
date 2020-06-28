import Utils.Drawing as Drawing
import math

class mplTurtle:
    
    def __init__(self,pos=(0,0),angle=0,draw=True):
        self.pos = pos
        self.angle = angle
        self.draw = draw
        
    def left(self,n):
        self.angle = (self.angle+n)%360
        
    def right(self,n):
        self.angle = (self.angle-n)%360
        
    def pen_up(self):
        self.draw = False
    
    def pen_down(self):
        self.draw = True
    
    def jump_to(self,pos):
        self.pos = pos
        
    def move_to(self,pos):
        if self.draw:
            Drawing.connect_p(self.pos,pos)
        else:
            self.pos = pos
    
    def set_angle(self,angle):
        self.angle = angle
        
    def forward(self,n):
        a = math.radians(self.angle)
        h = math.sin(a)*n
        w = math.cos(a)*n
        newpos = (self.pos[0]+h,self.pos[1]+w)
        Drawing.connect_p(self.pos,newpos)
        self.pos = newpos
        
    def get_pos(self):
        return self.pos
    
    def get_angle(self):
        return self.angle
    
    def get_draw(self):
        return self.draw