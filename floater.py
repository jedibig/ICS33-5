# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = speed = 5
    def __init__():
        Prey.__init__(self,x,y,self.radius,self.radius,0,self.speed)
        self.randomize_angle()

    def update():
        self.move()

    def display():
        x,y = self.get_location()
        blue = '#0000FF'
        canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius,fill=blue)