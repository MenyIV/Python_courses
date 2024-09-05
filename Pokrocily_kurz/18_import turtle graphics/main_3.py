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


tommy = Turtle()



tommy.shape("turtle")
tommy.pensize(5)




my_screen = Screen()
my_screen.bgcolor("black")

moves=2
while moves != 20:
    col=barva3()
    tommy.color(col,col)
    i=0
    
    for i in range (0,moves):
        tommy.forward(50)
        tommy.right(360/moves)
    moves +=1    




#print(tommy)
#print(f"{my_screen.canvwidth}x{my_screen.canvheight}")
my_screen.exitonclick()