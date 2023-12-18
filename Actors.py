import turtle

#Actors are in-game objects. Child class of the turtle module
class Actors(turtle.Turtle):
    #Default attributes for all actors
    def __init__(self, ashape, color, startX, startY):
        turtle.Turtle.__init__(self, shape = ashape)
        self.speed(0) #Animation speed
        self.penup() #Created actor should not draw anything on screen
        self.color(color) #Set actor color
        self.goto(startX, startY) #Set actor stating position
        self.speed = 1 #Movement speed
    
    #Actor movement
    def move(self):
        self.fd(self.speed)
        #Actor-Border collision detection
        if self.xcor() > 340:
            self.setx(339)
            self.rt(60)
        elif self.xcor() < -340:
            self.setx(-341)
            self.rt(60)
        elif self.ycor() > 290:
            self.sety(289)
            self.rt(60)
        elif self.ycor() < -290:
            self.sety(-291)
            self.rt(60)
    
    def stop(self):
        self.goto(-1000, 1000)
        self.speed = 0
        
    #Actor-Actor collision detection
    def collision(self, actor):
        if (self.xcor() <= actor.xcor() + 10) and (self.xcor() >= actor.xcor() - 10) and (self.ycor() <= actor.ycor() + 10) and (self.ycor() >= actor.ycor() - 10):
            return True
        else:
            return False