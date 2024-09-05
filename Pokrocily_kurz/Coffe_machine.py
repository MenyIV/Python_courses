#Opakování základů coffe machine

#Zeptá se co si dáš esspreso/latte/capuchino


#hlídá zbytek zdrojů resources
#Když bude málo napíše že nejsou zdroje
#po zadání report vypíše zbytek ztdrojů

from Coffe_machine_data import MENU
from Coffe_machine_data import resources
from Coffe_machine_data import kafe

import time

resources=resources
logo = kafe

def print_menu():
    print("Zadejte volbu nápoje:\n")
    menu=MENU.keys()
    number = 1
    for each in menu:
        print(f" {number} - {each}")
        number +=1       

def vhazovani(hodnoty_list):
    print ("Zadej počet vložených mincí:")
    vlozeno = 0
    for each in hodnoty_list:
        pocet = int(input (f"Vlož {each} \n"))
        vlozeno = vlozeno+int(each)*pocet
    return vlozeno
  
        
def mincovnik (cena):
    hodnoty_list = ["50","20","10","5"]
    print (f"cena kávy je {cena} Kč")
    vlozeno = vhazovani(hodnoty_list)
    
    if cena>vlozeno:
        print("Vhoď více mincí")
        vhazovani(hodnoty_list)
    elif cena<vlozeno:
        vratka = vlozeno - cena
        print (f"Hodnota kávy je {cena}")
        print (f"Vracím: {vratka}")
    else:
         print (f"Vložil jsi přesně {cena}")
    
def validate_resources(resources,ingredients):
    print (ingredients)
    print(resources)
    zdroje=resources.keys()
    print (zdroje)
    vysledek = True
    
    
    for each in zdroje:
        if resources[each]>ingredients[each]:
            print (f"{each} je OK")
            vysledek = True
        else:
            print (f"{each} není")
            hlaska(each)
            vysledek = False
            

    if vysledek == True:
        for each in zdroje:
            resources[each]=resources[each]-ingredients[each]
        
    return resources

def hlaska (zdroj):
    i=1
    while i == 1:
        print("Zavolejte servis !!!!!!!!!!!!!!!!!!\n")
        print(f"došlo {zdroj}")
        i=input()
   
def coffe_prepare(volba,resources,cena,logo):
    mincovnik(cena)
    
    print("Kafe se připravuje...")
    rows = logo.splitlines()
    for row in rows:
        print(row)
        time.sleep(0.5)


    
def automat(resources):
       
    print_menu()
    volba = input()
    seznam_kafe = {f'{i+1}': hodnota for i, (_, hodnota) in enumerate(MENU.items())}
    if volba == "report":
        print (resources)

    #hlavní program který vypíš reporty nebo zavolá kafemachine
    else:
        volba_ingredients=seznam_kafe[volba]
        print (volba_ingredients)
        cena = volba_ingredients['cost']
        ingredients= volba_ingredients['ingredients']
        resources = validate_resources(resources,ingredients)
        print(f"Zbývá {resources} zdrojů")
        coffe_prepare(volba,ingredients,cena,logo)
    
    return resources

next = "A"
 
while next == "A":
    resources = automat(resources)
    
    next = input ("Dáš si kafe A/N\n")  
    

