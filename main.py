from turtle import *

### CLASS and FUNCTION DEFINITIONS ###

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('white')
    pen.begin_fill()
    pen.goto(-120,250)
    pen.goto(120,250)
    pen.goto(120,-250)
    pen.goto(-120,-250)
    pen.goto(-120,250)
    pen.end_fill()

class Player(Turtle):
    def __init__(self,screen,color,bullets,rt_key,lt_key,f_key):
        super().__init__()
        self.ht()
        self.penup()
        self.color(color)
        self.bullets = []
        self.setheading(90)
        self.shape('turtle')
        self.st()
        screen.onkeypress(self.tright, rt_key)
        screen.onkeypress(self.tleft, lt_key)
        screen.onkeypress(self.fire, f_key)

    def tright():
        self.rt(10)

    def tleft():
        self.lt(10)

    def fire():
        self.bullets.append(Bullet(self))

class Bullet(Turtle):
    def __init__(self,color,bullets):
        super().__init__()
        self.ht()
        self.color(color)
    
    def move():
        self.fw(10)



### PROGRAM ###
screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
p1_bullets = []
p2_bullets = []
p1 = Player(screen,'red',p1_bullets,'d','a','f')
p2 = Player(screen,'blue',p2_bullets,'l','j',';')
playing_area()
p1.goto(-45,-220)
p2.goto(45,-220)



screen.exitonclick()