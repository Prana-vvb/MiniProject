import turtle
import random
import time
#from pydub import AudioSegment
#from pydub.playback import play

#Create screen
turtle.speed(0) #Set animation speed to max
turtle.bgcolor('black') #Set screen background color
#turtle.bgpic('BG.gif')
turtle.ht() #Hide the turtle created by default
turtle.Screen().getcanvas().winfo_toplevel().attributes('-fullscreen', True) #Open window in fullscreen by default
turtle.setundobuffer(1) #Reduce strain on system memory
turtle.tracer(0) #Increase drawing speed
store = open('High scores.txt', 'w')

maxSpeed = 6 #Set max speed of player
minSpeed = 0 #Set min speed of player

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

#Player class. Child of Actors
class Player(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.speed = 0 #Player start speed. Can be increased/decreased using accelerate/decelerate functions
    
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

#Enemies. Child of Actors  
class Enemy(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.speed = 5
        self.setheading(random.randint(0, 360))

#Friendlies. Child of Actors
class Ally(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.speed = 4
        self.setheading(random.randint(0, 360))

#Missiles/Bullets for the player
class Projectile(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000,1000)
        
    def fire(self):
        if self.status == 'ready':
            #play(AudioSegment.from_wav("projectileFire.wav"))
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status =  "firing"
            
    def move(self):
        if self.status == "firing":
            self.fd(self.speed) 
        #Border-Projectile collision check
        if self.xcor()<-340 or self.xcor() > 340 or self.ycor()<-290 or self.ycor() > 290 :
            self.goto(-1000,1000)
            self.status = 'ready'

class Particle(Actors):
    def __init__(self, ashape, color, startX, startY):
        Actors.__init__(self, ashape, color, startX, startY)
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

#Game info(Score, levels etc.)
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.high_score = 0
        if self.score > self.high_score:
            self.high_score = self.score
        store.write(str(self.high_score))
        self.pen = turtle.Turtle()
        self.hs = turtle.Turtle()
        self.liv = turtle.Turtle()
        self.lvl = turtle.Turtle()
        self.pen.speed(0)
        self.pen.ht()
        self.pen.color('white')
        self.hs.speed(0)
        self.hs.ht()
        self.hs.color('white')
        self.hs.goto(-1000, 1000)
        self.liv.speed(0)
        self.liv.ht()
        self.liv.color('white')
        self.liv.goto(-1000, 1000)
        self.lvl.speed(0)
        self.lvl.ht()
        self.lvl.color('white')
        self.lvl.goto(-1000, 1000)
        self.lives = 3

    #Draws the border for the playable game area
    def border(self):
        self.pen.pensize(4)
        self.pen.penup()
        self.pen.goto(-350, 300)
        self.pen.pendown()
        for i in range(2):
            self.pen.fd(700)
            self.pen.rt(90)
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()

    def status(self):
        self.pen.undo()
        self.hs.undo()
        self.liv.undo()
        self.lvl.undo()

        self.pen.penup()
        self.pen.goto(-350, 310)
        self.pen.write('Score: %s' %(self.score), font = ('Times New Roman', 20, 'normal'))
        
        self.hs.penup()
        self.hs.goto(200, 310)
        self.hs.write('High Score: %s' %(self.score), font = ('Times New Roman', 20, 'normal'))

        self.liv.penup()
        self.liv.goto(-350, -350)
        self.liv.write('Lives: %s' %(self.lives), font = ('Times New Roman', 20, 'normal'))

        self.lvl.penup()
        self.lvl.goto(280, -350)
        self.lvl.write('Level: %s' %(self.level), font = ('Times New Roman', 20, 'normal'))

    def exit(self):
        turtle.clearscreen()
        turtle.bgcolor('black')
        self.pen.goto(0, 0)
        self.pen.write('Thank you for playing!', font = ('Times New Roman', 35, 'normal'), align = 'center')
        time.sleep(1)
        turtle.bye()

game = Game() #Create game object
game.border() #Draw game border
game.status() #Display game stats(Score, player lives, level etc.)
player = Player('classic', 'white', 0, 0) #Create player object

enemies = []
for i in range(6):
    x = random.randint(-341, 339)
    y = random.randint(-291, 289)
    enemies.append(Enemy('circle', 'red', x, y)) #Create enemy objects

missile = Projectile("triangle", "yellow", 0, 0) #Create projectile object

allies = []
for i in range(6):
    x = random.randint(-341, 339)
    y = random.randint(-291, 289)
    allies.append(Ally("square", "blue", x, y)) #Create ally object

particles_e = []
for i in range(60):
    particles_e.append(Particle('circle', 'orange', 0, 0))

particles_a = []
for i in range(60):
    particles_a.append(Particle('circle', 'dodger blue', 0, 0))

particles = [particles_e, particles_a]

#Key bindings
turtle.onkey(player.turnL, 'Left')
turtle.onkey(player.turnL, 'a')

turtle.onkey(player.turnR, 'Right')
turtle.onkey(player.turnR, 'd')

turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.accelerate, 'w')

turtle.onkey(player.decelerate, 'Down')
turtle.onkey(player.decelerate, 's')

turtle.onkey(missile.fire, 'space')

turtle.onkey(game.exit, 'Escape')
turtle.listen()

#Main game loop
def main():
    while True:
        turtle.update()
        time.sleep(0.05)
        player.move()
        
        for enemy in enemies:
            enemy.move()
            #Checking Player-Enemy collision
            if player.collision(enemy):
                for p in particles_e:
                    p.start_exploding(enemy.xcor(), enemy.ycor())
                enemy.stop()
                game.score -= 25 #Loses less points because kamikaze lol
                game.lives -= 1
                game.status()

            #Checking Projectile-Enemy collision
            if missile.collision(enemy):
                enemy.stop()
                for p in particles_e:
                    p.start_exploding(missile.xcor(), missile.ycor())
                missile.goto(-1000, 1000)
                missile.status= "ready"
                game.score += 100
                game.status()

        missile.move()

        for ally in allies:
            ally.move()
            #Checking Player-Ally collision
            if player.collision(ally):
                for p in particles_a:
                    p.start_exploding(ally.xcor(), ally.ycor())
                ally.stop()
                game.score -= 50
                game.lives -= 1
                game.status()

            #Checking Projectile-Ally collision
            if missile.collision(ally):
                ally.stop()
                for p in particles_a:
                    p.start_exploding(missile.xcor(), missile.ycor())
                missile.goto(-1000, 1000)
                missile.status= "ready"
                game.score -= 50
                game.status()
        
        for parts in particles:
            for p in parts:
                p.move()
                #Checking Particle-Border collision
                if p.xcor()<-340 or p.xcor() > 340 or p.ycor()<-290 or p.ycor() > 290 :
                    p.goto(-1000, 1000)

if __name__ == '__main__':
    main()
