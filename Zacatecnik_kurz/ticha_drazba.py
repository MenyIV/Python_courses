import os
import operator
from logos import cheese

logo = cheese

omacka=["Pojďte dražit sejra"]

database = { "Jméno":"Příhoz",}
name=""
bet=""
prompt = ""

def better_name (first_name , second_name):
    if first_name == "" or second_name == "":
        return "Není zadáno jméno"
    full_name = first_name + " " + second_name
    return full_name.title()

def imput():
    name = better_name(input("Zadej svoje jméno\n"),input("Zadej svoje Příjmení\n"))
    bet = input("Jaký je tvůj příhoz? v Kč\n")
    if bet == "":
        promt = "A"
        return 
    database.update({name:bet})
    os.system('cls')
    #os.system("clear")
    return (name,bet)

while prompt != "N":
    
    # vypsat logo aukce a něajakou omáčku
    print(logo)
    i=0
    while i != 3:
        print("\n")
        i+=1
    print (omacka)
    i=0
    while i != 1:
        print("\n")
        i+=1
    
    prompt = input("Chceš zadat příhoz A/N\n")
    prompt=prompt.upper()
    
    if prompt == "A":
        imput()    

#Vyhodnocení aukce a vyhlášení výsledků
win_database= dict(sorted(database.items(), key=operator.itemgetter(1)))
#print (win_database)


for key in win_database:
    i=1
    win_user=key
    win_bet=win_database[key]
    if i == 1:
        break

print (f"Aukci vyhrává {win_user} s nejvyšším příhozem {win_bet} Kč. Gratulujeme")



 