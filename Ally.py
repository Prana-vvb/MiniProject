import Actors
import random

#Friendlies. Child of Actors
class Ally(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.Actors.__init__(self, ashape, color, startX, startY)
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.speed = 4
        self.setheading(random.randint(0, 360))