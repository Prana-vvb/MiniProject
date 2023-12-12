import turtle
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
#turtle.bgpic('BG.gif')
turtle.ht() #Hide the turtle created by default
turtle.Screen().getcanvas().winfo_toplevel().attributes('-fullscreen', True) #Open window in fullscreen by default
turtle.setundobuffer(1) #Reduce strain on system memory
turtle.tracer(0) #Increase drawing speed

game = Game.Game() #Create game object
game.border() #Draw game border
game.status() #Display game stats(Score, player lives, level etc.)
player = Player.Player('classic', 'white', 0, 0) #Create player object

enemies = []
for i in range(6):
    enemies.append(Enemy.Enemy('circle', 'red', -100, 0)) #Create enemy objects

missile = Projectile.Projectile("triangle", "yellow", 0, 0) #Create projectile object

allies = []
for i in range(6):
    allies.append(Ally.Ally("square", "blue", 200, 0)) #Create ally object

particles_e = []
for i in range(60):
    particles_e.append(Particle.Particle('circle', 'orange', 0, 0))

particles_a = []
for i in range(60):
    particles_a.append(Particle.Particle('circle', 'dodger blue', 0, 0))

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
                player.lives -= 1
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
                player.lives -= 1
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
