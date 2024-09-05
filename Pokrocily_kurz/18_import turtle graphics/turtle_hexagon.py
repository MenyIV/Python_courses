
from turtle import Turtle, Screen
import random
import turtle


def color(i):
    #tohle je spolehlivý ale generuje to málo barev
    barva = ["red","blue","green","white","magenta","orange"]
    return (f"{barva[i]}")


joy = Turtle()

my_screen = Screen()
my_screen.bgcolor("black")

x=0
y=0
forward = 10
for i in range(0,150):
    print (i)
    x= x-3
    y= 5+y
    x=x
    y=y
    for n in range (0,6):
        print(joy.position())
        joy.color(color(n))
        joy.forward(forward)
        joy.right(360/6)
    forward = forward+6
    joy.up()
    joy.setpos(x,y)
    #joy.setx(x)
    #joy.sety(y)
    joy.down()




my_screen.exitonclick()
