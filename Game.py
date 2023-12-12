import turtle
import time

#Game info(Score, levels etc.)
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.high_score = 0
        if self.score > self.high_score:
            self.high_score = self.score
        self.gameState = 'play'
        self.pen = turtle.Turtle()
        self.lives = 3
    
    #Draws the border for the playable game area
    def border(self):
        self.pen.speed(0)
        self.pen.ht()
        self.pen.color('white')
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
        self.pen.penup()
        self.pen.goto(-350, 310)
        self.pen.write('Score: %s' %(self.score), font = ('Times New Roman', 20, 'normal'))
        self.pen.goto(200, 310)
        self.pen.write('High Score: %s' %(self.score), font = ('Times New Roman', 20, 'normal'))
        self.pen.goto(-350, -350)
        self.pen.write('Lives: %s' %(self.lives), font = ('Times New Roman', 20, 'normal'))
        self.pen.goto(280, -350)
        self.pen.write('Level: %s' %(self.level), font = ('Times New Roman', 20, 'normal'))
    
    def exit(self):
        turtle.clearscreen()
        turtle.bgcolor('black')
        self.pen.pendown()
        self.pen.goto(0, 0)
        self.pen.write('Thank you for playing!', font = ('Times New Roman', 35, 'normal'), align = 'center')
        time.sleep(1)
        turtle.bye()