#tesovací soubor
from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("green")
screen.title("Vítejte v hadovi")
screen.setup(width=400,height=400)

screen.tracer(False)

squeare1 = Turtle("square")
squeare1.penup()
squeare1.goto(0,0)
squeare2 = Turtle("square")
squeare2.penup()
squeare2.goto(-20,0)

screen.update()

for i in range (0,80):
    squeare1.forward(10)
    squeare2.forward(10)
    time.sleep(0.1)
    screen.update()
    

screen.exitonclick()
screen.mainloop()