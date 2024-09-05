#kreslí N-hrany N+1
#každý obrazec jinou barvou

#funkce pro změnu barvy
from turtle import Turtle, Screen
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

def move (angles):
    #dostane kolika N-hran má nakreslit
    #spočítá kolikrát se bude měnit směr 
    #spočítá úhel
    col=barva3()
    tommy.color(col,col)
    angle=360/angles
    steps=angles
    i=0
    while i != steps:
        i+=1
        tommy.forward(50)
        tommy.right(angle)

tommy = Turtle()



tommy.shape("turtle")
tommy.pensize(5)




my_screen = Screen()
my_screen.bgcolor("black")


for step in range (2,20):
    move(step)
    




#print(tommy)
#print(f"{my_screen.canvwidth}x{my_screen.canvheight}")
my_screen.exitonclick()