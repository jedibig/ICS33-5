# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    def __init__(self, x, y):
        _image = PhotoImage(file='ufo.gif')
        Prey.__init__(self, x, y, graphic_file.width(), graphic_file.height(), 0, 5)
        self.randomize_angle()

    def update():
        if random() <= 0.3:
            self.set_velocity(min(7, max(3, self._speed + random()-0.5)), self._angle + random()-0.5 )
        self.move()

    def display(self,canvas):
       canvas.create_image(*self.get_location(),image=self._image)