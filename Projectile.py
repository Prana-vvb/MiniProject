import Actors
import Player
#from pydub import AudioSegment
#from pydub.playback import play

player = Player.Player('classic', 'white', 0, 0)
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
