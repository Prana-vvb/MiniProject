import turtle
import time

#Game info(Score, levels etc.)
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.pen = turtle.Turtle()
        self.hs = turtle.Turtle()
        self.liv = turtle.Turtle()
        self.lvl = turtle.Turtle()
        self.pen.speed(0)
        self.pen.ht()
        self.pen.color('white')
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

    #Displays game stats like Score, Lives etc.
    def status(self):
        self.pen.undo()
        self.hs.undo()
        self.liv.undo()
        self.lvl.undo()

        self.pen.penup()
        self.pen.goto(0, 310)
        self.pen.write('Score: %s' %(self.score), font = ('Times New Roman', 20, 'normal'), align = 'center')

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