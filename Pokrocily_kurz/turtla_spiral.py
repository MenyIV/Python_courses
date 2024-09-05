from turtle import Turtle,Screen

colors = ["red","blue","green","white","violet","orange","dark_blue"]

arrow = Turtle("arrow")
arrow_step = 20
arrow_nhran = 6
add_lenght = 2

for n in range (0,500):
    arrow.pencolor(colors[n%arrow_nhran])
    arrow.forward(arrow_step)
    arrow.right(360/arrow_nhran)
    arrow_step = add_lenght + arrow_step
    



screen = Screen()
screen.exitonclick()