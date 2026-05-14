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
    def __init__(self,screen,color,rt_key,lt_key,f_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.playercolor = color
        self.penup()
        self.color(color)
        self.bullets = []
        self.setheading(90)
        self.shape('turtle')
        self.st()
        screen.onkeypress(self.tright, rt_key)
        screen.onkeypress(self.tleft, lt_key)
        screen.onkeypress(self.fire, f_key)

    def tright(self):
        self.rt(10)

    def tleft(self):
        self.lt(10)

    def fire(self):
        self.bullets.append(Bullet(self))

class Block(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.ht()
        self.pu
        self.color('gray')
        self.shape('square')
        self.bullets = []
        self.health = 3
        self.goto(x,y)
        self.st()

    def damage(self):
        if self.health >= 0:
            if self.health == 2:
                self.color('orange')
            elif self.health == 1:
                self.color('red')
        else:
            self.ht()
            blocks.remove(self)
    def fall(self):
        self.seth(-90)
        self.fw(10)

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.playercolor)
        self.penup()
        self.goto(player.xcor(),player.ycor())
        self.setheading(player.heading())
        self.forward(20)
        self.st()
    
    
    def move(self,player):
        self.forward(15)
        
        if self.ycor() > 235 or self.ycor() < -235:
            self.speed(0)
            self.setheading(180 - turtle.heading())
            self.fd(10)
            self.speed(1)
            self.append(create_turtle())

        if self.xcor() > 235 or self.xcor() < -235:
            self.speed(0)
            self.setheading(180 - turtle.heading())
            self.fd(10)
            self.speed(1)
            self.append(create_turtle())


def update():
    for bullet in p2.bullets:
        bullet.move()
    for bullet in p1.bullets:
        bullet.move()
    for y in range(190,149,-20):
        for x in range(-40,41,20):
            blocks.append(Block(x,y))

    screen.ontimer(update,120)
### PROGRAM ###
screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.setup(520,520)
blocks = []
p1 = Player(screen,'red','d','a','f')
p2 = Player(screen,'blue','l','j',';')
playing_area()
p1.ht()
p1.goto(-45,-220)
p1.st()
p2.ht()
p2.goto(45,-220)
p2.st()

screen.onkey(update,'space')

screen.exitonclick()