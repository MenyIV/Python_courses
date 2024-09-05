#kalkulačka
#kalkulačka s dictionary

import os

def sum(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2

operations = {
    "+":sum,
    "-":subtract,
    "*":multiply,
    "/":devide
}
end = "A"
vysledek = 0

while end == "A":
    print ("startuji nový výpočet")
    n1 = float(input("Zadej prvni cislo pro vypocet a Enter\n"))
    task = "A"
    
    while task == "A":
        for each in operations:
            print(each)
        operator = input("Vyber operátor uvedený výše a Entr\n")
        n2 = float(input("Zadej druhecislo pro vypocet a Entr\n"))
    
    
        calc_function=operations[operator]  
        vysledek=calc_function(n1,n2)
    
        print(f"{n1}{operator}{n2}={vysledek}")
        task = input("Chceš pokračovat A/N")
        n1= vysledek
    end = input("Chceš nový výpočet? A/N\n")
    os.system("cls")

print ("Konec programu")