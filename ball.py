# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey): 
    radius = speed = 5

    def __init__(self,x,y):
        Prey.__init__(self,x,y,self.radius,self.radius,0,self.speed)
        self.randomize_angle()

    def update(self,model):
        self.move()
    
    def display(self,canvas):
        x,y = self.get_location()
        blue = '#0000FF'
        canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius,fill=blue)
