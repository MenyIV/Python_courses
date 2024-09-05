#chodí náhodně
#jako randomwalk
#zvětšuje se pensize až do nkroků


#funkce pro změnu barvy
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)

import random


def barva1():
    #tohle je spolehlivý ale generuje to málo barev
    barva = ["red","blue","green","white"]
    return (f"{barva[random.randint(0,int(len(barva)-1))]}")

def barva2():
    #tohle není moc spolehlivý páč to generuje aj čísla mimo rozsah
    hexcol1 = hex(random.randint(0,2**24))
    retcol= "#" + hexcol1[2:]
    print(retcol)             
    return(retcol)

def barva3():
    import secrets
    s= secrets.token_hex(3)
    s= "#"+s
    print(s)
    return(s)

def barva4():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    s=(r,g,b)
    return s


tommy = Turtle()



tommy.shape("turtle")
tommy.pensize(1)
uhlovani = (0,90,180,270,360)



my_screen = Screen()
my_screen.bgcolor("black")

i=1
while i != 100:
    col=barva4()
    tommy.color(col,col)
    tommy.forward(20)
    if i<10:
        tommy.pensize(i)
        tommy.speed(i*2)
    tommy.right(random.choice(uhlovani))
    i+=0.5




#print(tommy)
#print(f"{my_screen.canvwidth}x{my_screen.canvheight}")
my_screen.exitonclick()