#tesovací soubor
from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("green")
screen.title("Vítejte v hadovi")
screen.setup(width=400,height=400)

screen.tracer(False)

#Hadí hlava
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(50,50)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+10)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-10)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+10)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-10)

#funkce

def moveup():
    head.direction = "up"  
def movedown():
    head.direction = "down"
def moveleft():
    head.direction = "left"
def moveright():
    head.direction = "right"
def stop():
    head.direction = "stop"

def apple_place():
    apple.goto(random.randint(-200,200),random.randint(-200,200))
    
def add_body():
    pass    
    
screen.listen()
screen.onkeypress(moveup,"w")
screen.onkeypress(movedown,"s")
screen.onkeypress(moveleft,"a")
screen.onkeypress(moveright,"d")
screen.onkeypress(stop,"space")
    


    

#hlavní cyklus
while Turtle:

    move()
    if head.distance(apple) < 20:
        print("kolize")
        apple_place()
    time.sleep(0.1)
    screen.update()




screen.exitonclick()
screen.mainloop()