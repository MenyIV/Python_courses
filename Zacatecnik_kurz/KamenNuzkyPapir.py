#hra kamen nuzky papir s PC

# Rock Paper Scissors ASCII Art

import random

# Rock

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



player = int(input("Vyber si volbu\n1=kámen\n2=papír\n3=nůžky\n"))
computer = random.randrange(1,4,1)

print (f"Hráč zvolil {player}")
print (f"Počítač zvolil {computer}")

lose1 = ["1","2"]
lose2 = ["2","3"]
lose3 = ["3","1"]
lose = [lose1,lose2,lose3]

plichta = [["1","1"],["2","2"],["3","3"]]

choose = [f"{player}",f"{computer}"]

if int(player) == 1:
    playericon = rock
elif player == 2:
    playericon = paper
else:
    playericon = scissors

if int(computer) == 1:
    computericon = rock
elif computer == 2:
    computericon = paper
else:
    computericon = scissors

print (f"hráč volí{playericon}")
print (f"počítač volí{computericon}")


#print (f"lose{lose}")
#print (f"choose{choose}")



if choose in lose:
    print ("prohra")
elif choose in plichta:
    print ("plichta")
else:
    print ("výhra")