#želva co nakreslí spirograf kolem dokola
#s každým kolem mění barvu
#lze zadat počet kruhů na 360° 
#musí se zastavit a čekat co bude

from turtle import Turtle, Screen
import turtle


joy = Turtle()


def barva():
    import secrets
    s= secrets.token_hex(3)
    s= "#"+s
    print(s)
    return(s)

def barva_choose(case):
    match case:
        case 1:
            joy.pencolor("yellow")
        case 2:
            joy.pencolor("green")

def spirograpf(pocet_kruhu,velikost_kruhu,facets):
    i=0

    while i != pocet_kruhu:
    
        joy.pencolor(barva())
        joy.setheading(i*(360/pocet_kruhu))
        joy.circle(velikost_kruhu,360,facets)
    
        i+=1

def spirograpf_2(pocet_kruhu,velikost_kruhu,facets,roztec):
    i=0

    while i != pocet_kruhu:
        
        
        joy.pencolor(barva())
        
        #joy.setheading(i*(360/pocet_kruhu))
        joy.circle(velikost_kruhu+(i*roztec),360,facets)
        joy.penup()
        joy.sety(-roztec*i)
        joy.pendown()
        i+=1
        
def spirograpf_3(pocet_kruhu,velikost_kruhu,facets,roztec):
    #cele prepsat tak aby to dělalo soustředné šestihrany
    #každá hrana změní barvu pokaždé stejně choose
    

    i=0
    
    while i != pocet_kruhu:
        moves = facets
        for n in range (0,moves):
            joy.forward(velikost_kruhu)
            joy.pencolor(barva_choose(i))
            joy.right(360/moves)
            moves +=1    

    joy.penup()
    joy.sety(-roztec*i)
    joy.pendown()
    i+=1

pocet_kruhu = 50
velikost_kruhu =5
facets = 2
roztec = 10
joy.shape("turtle")
joy.hideturtle()
joy.pensize(1)
joy.speed(5)
my_screen = Screen()
my_screen.bgcolor("black")




spirograpf_3(pocet_kruhu,velikost_kruhu,facets,roztec)
my_screen.exitonclick()