from turtle import *
import time, random

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
    def __init__(self,x,y,screen,color,rt_key,lt_key,f_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.playercolor = color
        self.penup()
        self.goto(x,y)
        self.color(color)
        self.playercolor = color
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
    def __init__(self,x,y,color,tipe):
        super().__init__()
        self.ht()
        self.seth(-90)
        self.pu()
        self.type = tipe
        self.speed(0)
        self.pencolor("black")
        self.turtlesize(2,2,2)
        self.color(color)
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
        elif self.health == 0 and self.type != 'bomb':
            blocks.remove(self)
            self.ht()
        elif self.health == 2 and self.type == 'bomb':
            self.ht()
            blocks.remove(self)
            
    def fall(self):
        self.forward(40)

class Bullet(Turtle):
    def __init__(self,player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.playercolor)
        self.penup()
        self.goto(player.xcor(),player.ycor())
        self.setheading(player.heading())
        self.forward(20)
        self.st()
    
    
    def move(self,turtle):
        self.forward(5)
        
        if self.ycor() > 250 or self.ycor() < -250:
            self.speed(0)
            self.setheading(180 - turtle.heading())
            self.fd(10)
            self.speed(0)
            

        if self.xcor() > 120 or self.xcor() < -120:
            self.speed(0)
            self.setheading(180 - turtle.heading())
            self.fd(10)
            self.speed(0)
        
    def hit(self,blocks,player):
        for block in blocks:
            if self.distance(block) <= 35:
                player.bullets.remove(self)
                self.ht()
                block.health -= 1
                block.damage()
                



def update():
    global start, blocks
    if time.time() - start > 2:
        start = time.time()
        screen.tracer(0)
        for block in blocks:
            block.fall()
        for x in range(-80,101,40):
            tipe = random.randint(1,15)
            if tipe == 1:
                blocks.append(Block(x,220,"green",'bomb'))
            elif len(blocks)%3==0 and tipe != 1:
                blocks.append(Block(x,220,"light gray",'normal'))
            elif len(blocks)%3==1 and tipe != 1:
                blocks.append(Block(x,220,"gray",'normal'))
            else:
                blocks.append(Block(x,220,"dark gray",'normal'))
        screen.tracer(1)

    for bullet in p2.bullets:
        bullet.move(p2)
        bullet.hit(blocks,p2)
    for bullet in p1.bullets:
        bullet.move(p1)
        bullet.hit(blocks,p1)
    

    screen.ontimer(update,80)
### PROGRAM ###
screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.setup(520,520)
start = time.time()
blocks = []
playing_area()
p1 = Player(-45,-220,screen,'red','d','a','f')
p2 = Player(45,-220,screen,'blue','l','j',';')




screen.onkey(update,'space')
screen.tracer(0)
for y in range(140,225,40):
    for x in range(-80,101,40):
        if len(blocks)%3==0:
            blocks.append(Block(x,y,"light gray",'normal'))
        elif len(blocks)%3==1:
            blocks.append(Block(x,y,"gray",'normal'))
        else:
            blocks.append(Block(x,y,"dark gray",'normal'))
screen.tracer(1)

screen.exitonclick()