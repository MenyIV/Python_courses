from turtle import Turtle, Screen


tommy = Turtle()
jerry = Turtle()

tommy.shape("turtle")
tommy.color("#906090","green")
tommy.pensize(7)


jerry.shape("circle")
jerry.color("yellow","red")


my_screen = Screen()
my_screen.bgcolor("black")

#i=0
#while i != 4:
#    jerry.forward(100)
#    jerry.right(90)
#    i+=1
size = 1
for _ in range (0,100):
    size += 1
    for _ in range (0,1):
        
        tommy.pensize(size)
        tommy.forward(10)
        tommy.up()
        tommy.forward(10)
        tommy.down()
    




#print(tommy)
#print(f"{my_screen.canvwidth}x{my_screen.canvheight}")
my_screen.exitonclick()