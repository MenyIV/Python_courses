#logo hacka
#PC si myslí číslo
#vyber obtížnost easy/hard
#pak se hádá a vyhodnocuje zda se hráč trefil
#vysoke nebo nízké


# dodělat dalsi hra? - šlo by naondit na manipulaci s tim konec = 0 a hru hodit do funkce
#včetně clearu motitoru

from logos import hadacka
import random
import os

guess_min = 1
guess_max = 50
konec = 0
logo = hadacka

pocet_pokusu = {
    "1":20,
    "2":15,
    "3":10,
    "4":5,
    "5":3
}

def scoring(guess_PC,tip,difficult):
    zbyva_pokusu = difficult -1
    if tip != guess_PC and difficult != 0:
        print("To ses netrefil\n")
        hiORlow (guess_PC,tip)
        print (f"Pocet zbyvajicich pokusu = {zbyva_pokusu}\n")
    else:
        print("Rozhoduji ....")
        winORlose(difficult)
    return zbyva_pokusu

def hiORlow (guess_PC,tip):
    if tip > guess_PC:
        print("Tip je příliš vysoký")
    else:
        print("Tip je příliš nízký")

def winORlose(difficult):
    global konec
    konec = 1
    if difficult != 0:
        print("vyhrál jsi")
    else:
        print("Prohra")
    


print(logo)



def hra():
    print(f"PC si myslí číslo od {guess_min} do {guess_max}\n")
    guess_PC = random.randint(guess_min,guess_max)

    print(f"PC si myslí {guess_PC}\n")

    dificulty = input(f"vyber si obtížnost 1-5\n")
    difficult = pocet_pokusu[dificulty]




    while difficult != 0 and konec == 0:
        tip = int(input ("Zadej tip\n"))
        print (f"Tvuj tip = {tip}\n")
        difficult = scoring(guess_PC,tip,difficult)   


hra()

dalsi = input ("Chceš hrát daší hru? A/N")

if dalsi == "A":
    os.system("cls")
    konec = 0
    hra()
else:
    print ("Konec hry")
    






    