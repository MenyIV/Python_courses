from turtle import Turtle,Screen

colors = ["red","blue","green","white","violet","orange","dark_blue"]



arrow = Turtle("arrow")
arrow_step = 20
pocet_barev = 6
n_hran = 6

for n in range (0,500):
    arrow.color(colors[n%pocet_barev])
    arrow.begin_fill()
    for i in range (0,n_hran):
        arrow.forward(arrow_step)
        arrow.right(360/n_hran)
    arrow.end_fill()
    



screen = Screen()
screen.exitonclick()