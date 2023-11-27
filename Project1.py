import os
import turtle
import random

#Create screen
turtle.speed(0) #Set animation speed to max
turtle.bgcolor('black') #Set screen background color
turtle.ht() #Hide the turtle created by default
turtle.setundobuffer(1) #Reduce strain on system memory
turtle.tracer(1) #Increase drawing speed

#Actors are in-game objects. Child class of the turtle class
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

#Player class. Child of Sprites
class Player(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.speed = 0 #Player start speed. Can be increased/decreased using accelerate/decelerate functions
        self.lives = 3 #Default player lives
    
    #Define player movement functions
    def turnL(self):
        self.lt(45)
    
    def turnR(self):
        self.rt(45)
    
    def accelerate(self):
        self.speed += 1
    
    def decelerate(self):
        self.speed -= 1


player = Player('classic', 'white', 0, 0) #Create player object

#Key bindings
turtle.onkey(player.turnL, 'Left')
turtle.onkey(player.turnL, 'a')

turtle.onkey(player.turnR, 'Right')
turtle.onkey(player.turnR, 'd')

turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.accelerate, 'w')

turtle.onkey(player.decelerate, 'Down')
turtle.onkey(player.decelerate, 's')
turtle.listen()

#Main game loop
def main():
    while True:
        player.move()

if __name__ == '__main__':
    main()
    
    
    
    