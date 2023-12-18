import Actors
import random

#Particles to display on Actor-Actor collision
class Particle(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.Actors.__init__(self, ashape, color, startX, startY)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.goto(-1000, 1000)
        self.frame = 0
    
    def start_exploding(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1
        
    def move(self):
        if self.frame > 0 and self.frame <= 10:
                self.fd(30)
                self.frame += 1
        else:
            self.frame = 0
            self.goto(-1000, 1000)
