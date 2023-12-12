import Actors

maxSpeed = 6 #Set max speed of player
minSpeed = 0 #Set min speed of player

#Player class. Child of Actors
class Player(Actors.Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.Actors.__init__(self, ashape, color, startX, startY)
        self.speed = 0 #Player start speed. Can be increased/decreased using accelerate/decelerate functions
        self.lives = 3 #Default player lives
    
    #Define player movement functions
    def turnL(self):
        self.lt(45)
    
    def turnR(self):
        self.rt(45)
    
    def accelerate(self):
        if self.speed < maxSpeed:
            self.speed += 1
    
    def decelerate(self):
        if self.speed > minSpeed:
            self.speed -= 1
