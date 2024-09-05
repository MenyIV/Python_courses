from data import data
import random
import os

# vypíše ten má tolik foloweru -OK
# a zeptá se kolik myslíš že má tenhle vín nebo míň? -OK

# na začátku vybereme jedno libovolného
# funkce pro výběr jednoho random údaje
# funkce pro porovnání má víc má míň


#tuningy
# pamatuje si poslední volbu -OK

# udělat tak aby se nemohly potkat dva stejné
# bodování - jak kam co

pokracuj = "A"
backloop = ""


def vyber (backloop):
    #zapamatovat minulá data a ty nevracet
    vypis = (data[random.randint(0,len(data)-1)])
    if backloop == vypis:
        vypis = vyber(backloop)
    else:
        print()
    #delka_dat = len(data)-1
    #vybrana_data = data[random.randint(0,delka_dat)]
    #return vybrana_data
    return vypis

def vypis_oznam(data):
    jmeno =data["name"]
    sledujici =data["follower_count"]
    print(f"{jmeno} ma {sledujici} sledujicich")
    
def vypis_dotaz(data):
    jmeno = data["name"]
    volba = input(f"{jmeno} má podle tebe více H nebo méně L sledujících\n")
    return volba

def vypis_vysledek(data1,data2):
        print(f"{data1['name']} ma {data1['follower_count']} sledujicich, proti tomu {data2['name']} ma {data2['follower_count']} sledujicich ")


def porovnani(data1,data2,volba):
    if data1["follower_count"] > data2["follower_count"] and volba == "L":
        print("ANO je to tak")
        vypis_vysledek(data1,data2)
        
        
    elif data1["follower_count"] < data2["follower_count"] and volba == "H":
        print("ANO je to tak")
        vypis_vysledek(data1,data2)
    else:
        print("Není to tak")
        vypis_vysledek(data1,data2)


#přeješ si pokračovat ANO/NE
data1=vyber(backloop)
while pokracuj == "A":
    data2=vyber(backloop)
    vypis_oznam(data1)
    volba = vypis_dotaz(data2)
    porovnani(data1,data2,volba)
    pokracuj = input("Chceš pokračovat A/N\n")
    data1=data2
    backloop=data1
else:
    os.system("cls")
    print("Děkuji za hru" )
    
    



