import os
import turtle
import random

#Create screen
turtle.speed(0) #Set animation speed to max
turtle.bgcolor('black') #Set screen background color
turtle.ht() #Hide the turtle created by default
turtle.setundobuffer(1) #Reduce strain on system memory
turtle.tracer(0) #Increase drawing speed

maxSpeed = 6
minSpeed = 0

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
        
    #Actor-Actor collision detection
    def collision(self, actor):
        if (self.xcor() <= actor.xcor() + 10) and (self.xcor() >= actor.xcor() - 10) and (self.ycor() <= actor.ycor() + 10) and (self.ycor() >= actor.ycor() - 10):
            return True
        else:
            return False

#Player class. Child of Actors
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
        if self.speed < maxSpeed:
            self.speed += 1
    
    def decelerate(self):
        if self.speed > minSpeed:
            self.speed -= 1

#Enemy class. Child of Actors  
class Enemies(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.speed = 1
        self.setheading(random.randint(0, 360))
        
class Ally(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.speed = 1
        self.setheading(random.randint(0, 360))
        
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
                self.rt(10)

#Bullets/Missiles for the player
class Projectile(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000,1000)
        
    def fire(self):
        if self.status == 'ready':
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status =  "firing"
            
    def move(self):
        
        if self.status == "firing":
            self.fd(self.speed) 
        #border check
        if self.xcor()<-290 or self.xcor() > 290 or \
            self.ycor()<-290 or self.ycor() > 290 :
            self.goto(-1000,1000)
            self.status = 'ready'
            
#Game info(score, levels etc.)
class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.gameState = 'play'
        self.pen = turtle.Turtle()
        self.lives = 3

    #Draws the border of the playable game area
    def border(self):
        self.pen.speed(0)
        self.pen.ht()
        self.pen.color('white')
        self.pen.pensize(4)
        self.pen.penup()
        self.pen.goto(-310, 300)
        self.pen.pendown()
        for i in range(2):
            self.pen.fd(700)
            self.pen.rt(90)
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
        
    def show_status(self):
        self.pen.undo()
        msg = "score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-320,310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

player = Player('classic', 'white', 0, 0) #Create player object
#enemy = Enemies('circle', 'red', -100, 0 )#Create enemy object
missile = Projectile("triangle", "yellow", 0, 0)#creating missile
#ally= Ally("square", "blue", 100, 0)#creating ally

enemies = []
for i in range(6):
    enemies.append(Enemies("square","red",-100,0))
    
allies = []
for i in range(3):
    allies.append(Ally("circle","blue", 100, 0))
    
game = Game() #Create game object
game.border() #Draw game border
game.show_status() #Show the game stats

#Key bindings
turtle.onkey(player.turnL, 'Left')
turtle.onkey(player.turnL, 'a')

turtle.onkey(player.turnR, 'Right')
turtle.onkey(player.turnR, 'd')

turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.accelerate, 'w')

turtle.onkey(player.decelerate, 'Down')
turtle.onkey(player.decelerate, 's')

turtle.onkey(missile.fire, "space")
turtle.listen()

#Main game loop
def main():
    while True:
        turtle.update()
        player.move()
        missile.move()
        
        for enemy in enemies:
            enemy.move()
            #checking collision player enemy
            if player.collision(enemy):
                enemy.goto(random.randint(-300, 300), random.randint(-250, 250)) #For collision testing purposes. Do not use in final
                #score increase
                game.score -= 100
                game.show_status( )
                
             #collsion missile-enemy
            if missile.collision(enemy):
                enemy.goto(random.randint(-300, 300), random.randint(-250, 250))
                missile.status= "ready" 
                game.score += 100
                game.show_status() 
            
                
        for ally in allies:
            ally.move()
            
            #collsion missile-ally
            if missile.collision(ally):
                ally.goto(random.randint(-300, 300), random.randint(-250, 250))
                missile.status= "ready" 
                #score decrease
                game.score -= 50
                game.show_status()
            
        #checking collision player enemy
        if player.collision(enemy):
            enemy.goto(random.randint(-300, 300), random.randint(-250, 250)) #For collision testing purposes. Do not use in final
            #score increase
            game.score -= 100
            game.show_status()
        #collsion missile-enemy
        if missile.collision(enemy):
            enemy.goto(random.randint(-300, 300), random.randint(-250, 250))
            missile.status= "ready" 
            game.score += 100
            game.show_status() 
            
        #collsion missile-ally
        if missile.collision(ally):
            ally.goto(random.randint(-300, 300), random.randint(-250, 250))
            missile.status= "ready" 
            #score decrease
            game.score -= 50
            game.show_status()

if __name__ == '__main__':
    main()
