from turtle import Turtle,Screen

colors = ["red","blue","green","white","violet","orange","dark_blue"]



arrow = Turtle("arrow")
point = Turtle("classic")
point_step = 3



pocet_barev = 6
zakladni_rad = 10
circle_rad = zakladni_rad + point_step

point.color("blue")


arrow.color("red")
arrow.begin_fill()
arrow.circle(10)
arrow.end_fill()

point.color("blue")
point.shape("classic")


for n in range (0,10):
    
    point.pencolor(colors[n%pocet_barev])
    point.circle(circle_rad)
    circle_rad=circle_rad+point_step



screen = Screen()
screen.exitonclick()