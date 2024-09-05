#Calculator

import os
#kalkulačka která se zeptá na oprátor na provede v následujícím kroku
#takže asi funkce která dostane oprátor; číslo jako vstup a vrátí výsledek
vysledek = 0
cislo1 = float(input("Zadej prvni cislo pro vypocet a Enter\n"))
task = "A"


def calc (cislo1,cislo2,operator):
    #funkce pro výpočet
    if operator == "+":
        return cislo1 + cislo2
    elif operator == "-":
        return cislo1 - cislo2
    elif operator == "*":
        return  cislo1 * cislo2
    elif operator == "/":
        return  cislo1 / cislo2
    else:
        return 1111101000
  



while task == "A":

    operator = input(f"+\n-\n*\n/\nVyber operátor uvedený výše")
    cislo2 = float(input("Zadej druhecislo pro vypocet a Entr\n"))
    
    vysledek = calc(cislo1,cislo2,operator)
    print(f"{cislo1}{operator}{cislo2}={vysledek}")
    task = input("Chceš pokračovat A/N")
    cislo1=vysledek
    os.system("cls")

print("Konec programu")












print ("Konec programu")