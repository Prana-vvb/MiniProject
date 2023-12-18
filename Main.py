import turtle
import random
import time
import Game
import Player
import Projectile
import Enemy
import Ally
import Particle

#Create screen
turtle.speed(0) #Set animation speed to max
turtle.bgcolor('black') #Set screen background color
turtle.bgpic('BG.gif')
turtle.ht() #Hide the turtle created by default
turtle.Screen().getcanvas().winfo_toplevel().attributes('-fullscreen', True) #Open window in fullscreen by default
turtle.setundobuffer(1) #Reduce strain on system memory
turtle.tracer(0) #Increase drawing speed

ECOUNT = 3 #Set default enemy count
ACOUNT = 3 #Set default ally count

game = Game.Game() #Create game object
game.border() #Draw game border
game.status() #Display game stats(Score, player lives, level etc.)
player = Player.Player('classic', 'white', 0, 0) #Create player object

enemies = []
allies = []

def create_e(c):
    for i in range(c):
        x = random.randint(-341, 339)
        y = random.randint(-291, 289)
        enemies.append(Enemy('circle', 'red', x, y))

def create_a(c):
    for i in range(c):
        x = random.randint(-341, 339)
        y = random.randint(-291, 289)
        allies.append(Ally("square", "blue", x, y))

create_e(ECOUNT) #Create enemy objects
create_a(ACOUNT) #Create ally objects

missile = Projectile("triangle", "yellow", 0, 0) #Create projectile object

#Create collision particles
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
    global ECOUNT
    global ACOUNT
    #Initialise local variables to count enemies and allies
    count_e = ECOUNT
    count_a = ACOUNT
    pen = turtle.Turtle()
    pen.color('white')
    pen.penup()
    pen.ht()

    #Display game title and player instructions
    pen.goto(-560, 0)
    pen.write('Spacewar!', font = ('Times New Roman', 35, 'normal'), align = 'center')
    pen.goto(560, 200)
    pen.write('How to play', font = ('Times New Roman', 30, 'normal'), align = 'center')
    pen.goto(560, 100)
    pen.write('Use W/A/S/D or the arrow keys', font = ('Times New Roman', 20, 'normal'), align = 'center')
    pen.goto(560, 70)
    pen.write('to move', font = ('Times New Roman', 20, 'normal'), align = 'center')
    pen.goto(560, -20)
    pen.write('Use the spacebar or the Enter key', font = ('Times New Roman', 20, 'normal'), align = 'center')
    pen.goto(560, -50)
    pen.write('to shoot', font = ('Times New Roman', 20, 'normal'), align = 'center')
    pen.goto(560, -140)
    pen.write('Shoot down your enemies(red)', font = ('Times New Roman', 20, 'normal'), align = 'center')
    pen.goto(560, -170)
    pen.write('while avoiding friendlies(blue)', font = ('Times New Roman', 20, 'normal'), align = 'center')

    while True:
        turtle.update()
        time.sleep(0.05)
        player.move()

        #Level check
        if count_e == 0:
            game.level += 1
            game.status()
            count_a = ACOUNT + game.level
            count_e = ECOUNT + game.level
            create_a(count_a)
            create_e(count_e)
        
        for enemy in enemies:
            enemy.move()
            #Checking Player-Enemy collision
            if player.collision(enemy):
                for p in particles_e:
                    p.start_exploding(enemy.xcor(), enemy.ycor())
                enemy.stop()
                game.score -= 25 #Loses less points because kamikaze lol
                game.lives -= 1
                count_e -= 1
                game.status()

            #Checking Projectile-Enemy collision
            if missile.collision(enemy):
                enemy.stop()
                for p in particles_e:
                    p.start_exploding(missile.xcor(), missile.ycor())
                missile.goto(-1000, 1000)
                missile.status= "ready"
                game.score += 100
                count_e -= 1
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
                count_a -= 1
                game.status()

            #Checking Projectile-Ally collision
            if missile.collision(ally):
                ally.stop()
                for p in particles_a:
                    p.start_exploding(missile.xcor(), missile.ycor())
                missile.goto(-1000, 1000)
                missile.status= "ready"
                game.score -= 50
                count_a -= 1
                game.status()
        
        for parts in particles:
            for p in parts:
                p.move()
                #Checking Particle-Border collision
                if p.xcor()<-340 or p.xcor() > 340 or p.ycor()<-290 or p.ycor() > 290 :
                    p.goto(-1000, 1000)

        #End game if player loses all lives
        if game.lives == 0:
            turtle.clearscreen()
            turtle.bgcolor('black')
            pen.goto(0, 30)
            pen.write('Game Over', font = ('Times New Roman', 35, 'normal'), align = 'center')
            pen.goto(0, -30)
            pen.write('Thank you for playing!', font = ('Times New Roman', 35, 'normal'), align = 'center')
            time.sleep(5)
            turtle.bye()

if __name__ == '__main__':
    main()
