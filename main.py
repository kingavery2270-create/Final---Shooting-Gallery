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
        self.score = 0
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

    def damage(self,player):
        if self.type == 'bomb':
            self.ht()
            blocks.remove(self)
            player.score += 1
            self.explode()
        if self.health > 0:
            if self.health == 2:
                self.color('orange')
            elif self.health == 1:
                self.color('red')
        elif self.health == 0 and self.type != 'bomb':
            self.ht()
            blocks.remove(self)
            player.score += 1
        

    def fall(self):
        self.forward(40)

    def explode(self):
        # if time.time()- self.start >2:
        tracer(0)
        for block in blocks:
            if self.distance(block) <= 80:
                block.ht()
                blocks.remove(block)
        tracer(1)

class Bullet(Turtle):
    def __init__(self,player):
        super().__init__()
        self.ht()
        self.score = 0
        self.speed(0)
        self.color(player.playercolor)
        self.penup()
        self.goto(player.xcor(),player.ycor())
        self.setheading(player.heading())
        self.forward(20)
        self.player =player
        self.st()
    
    def die(self):
        self.ht()
        if bullet in self.player.bullets:
            self.player.bullets.remove(self)        

    def move(self):
        self.forward(15)
        
        if self.ycor() > 250 or self.ycor() < -250:
            self.die()
            

        if self.xcor() > 120 or self.xcor() < -120:
            self.speed(0)
            self.setheading(180 - self.heading())
            self.fd(10)
            self.speed(0)
        

# def hit(self,player):
#     for block in blocks:
#         if block.distance(self) <= 35:
#             self.ht()
#             if bullet in player.bullets:
#                 self.die()
#             block.health -= 1
#             block.damage(player)
def setscoreboard():
            yertle = Turtle()
            yertle.ht()
            yertle.speed(0)
            yertle.begin_fill()
            yertle.color('light gray')
            yertle.penup()
            yertle.goto(-110,-240)
            yertle.pendown()
            yertle.goto(110,-240)
            yertle.goto(110,-210)
            yertle.goto(-110,-210)
            yertle.goto(-110,-240)
            yertle.end_fill()

def endscreen():
    end = Turtle()
    end.ht()
    end.speed(0)
    end.color('light gray')
    end.goto(-85,40)
    end.begin_fill()
    end.goto(85,40)
    end.goto(85,-40)
    end.goto(-85,-40)
    end.goto(-85,40)
    end.goto(-83,-37)
    end.end_fill()
    end.color('black')
    end.write('GAME OVER',font=['Arial',20,'normal'])
    end.color('light gray')
    end.penup()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color('black')
        self.speed(0)
        self.begin_fill()
            
    def printscore(self,player,x):
        self.pu()
        self.goto(x,-240)
        self.color('black')
        self.pd()
        self.write(player.score,font=['Arial',20,'normal'])


def update():
    global start, blocks, bullet, block, game
    if game:
        if time.time() - start > 2:
            start = time.time()
            screen.tracer(0)
            for block in blocks:
                block.fall()
                if block.ycor() < -160:
                    blocks.clear()
                    p1.ht()
                    p2.ht()
                    game= False
                    

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
        p1score.printscore(p1,-80)
        p2score.printscore(p2,80)
        for bullet in p2.bullets:
            bullet.move()
            for block in blocks:
                p2currentscore = p2.score
                if block.distance(bullet) <= 35:
                    bullet.die()
                    block.health -= 1
                    block.damage(p2)
                if p2.score > p2currentscore:
                    p2score.clear()
                    p2score.printscore(p1,-80)
            
        for bullet in p1.bullets:
            bullet.move()
            for block in blocks:
                p1currentscore = p1.score
                if block.distance(bullet) <= 35:
                    bullet.die()
                    block.health -= 1
                    block.damage(p1)
                if p1.score > p1currentscore:
                    p1score.clear()
                    p1score.printscore(p1,-80)
    else:
        endscreen()

    screen.ontimer(update,80)
### PROGRAM ###
screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.setup(520,520)
start = time.time()
blocks = []
playing_area()
p1 = Player(-45,-180,screen,'red','d','a','f')
p2 = Player(45,-180,screen,'blue','l','j',';')
p1score = Score()
p2score = Score()
game = True


screen.onkey(update,'space')
screen.tracer(0)
for y in range(140,225,40):
    for x in range(-80,101,40):
        tipe = random.randint(1,15)
        if tipe == 1:
            blocks.append(Block(x,220,"green",'bomb'))
        elif len(blocks)%3==0 and tipe > 1:
            blocks.append(Block(x,220,"light gray",'normal'))
        elif len(blocks)%3==1 and tipe > 1:
            blocks.append(Block(x,220,"gray",'normal'))
        else:
            blocks.append(Block(x,220,"dark gray",'normal'))
screen.tracer(1)
setscoreboard()
screen.exitonclick()