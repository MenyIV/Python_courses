# Hra šibenice se jmény z harryho pottera
# program napsaný bez funkcí

#nereaguje na malá a velká písmena
#nejde vzrát pokus se opakuje písmenko např.: BRUMB8L

#lower case uppercase if je to první znak tak upper jinak lower
#a taky by se dalo vymyslet chceš hrát znovu? Y/N
#dodělat životy 6

import random
import math

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters_list = letters
word_list = ["Ron","Hermiona","Harry","Hagrid","Brumbál"] 
sibenice_list_guess=[]
sibenice_list=[]
zivoty = 6

#vybere slovo k uhodnuti
word_guess = random.choice(word_list)
print (f"Myslím si slovo. Které má {len(word_guess)} zanků\n")
print (f"vybrané slovo: {word_guess.upper()}")

#posklada pocet carek v sibenici
#rozloží slovo do listu a převede na velká písmena
for sibenice in range (0,len(word_guess)):
    sibenice_list_guess.append("_ ")
    sibenice_list.append(word_guess[sibenice].upper())
    
# #převedení na velká písmena
# for each in sibenice_list:
#     sibenice_list_upper = []
#     sibenice_list_upper.append(each.upper())
   
    
    
#print (f"rozebrano do listu{sibenice_list}")

#nabidne pismena k hadani
#print(f"před podmínkou1:{sibenice_list}2:{sibenice_list_guess}")
while sibenice_list != sibenice_list_guess:
    guess_chart_value = str(input ("vyber si pismenko k hadani:")).upper()
    #print(f"za podmínkou1:{sibenice_list}2:{sibenice_list_guess}")
    # vymeni hledane pismenko v abecede
    try:
        pozice = letters.index(guess_chart_value)
    except ValueError:
        print("Písmeno není v nabídce")
        
    #print(f"Pismeno{guess_chart_value} je na {pozice+1} pozici v abecedě")
    letters[pozice] = "❌"
    print(letters)

    #napise na spravnou pozici uhlazeneho vystupu
    #teď by to mělo běhat ve smyčce
    #overi pozici ve vystupu a prepise__

    #OPRAVA CHYBY czklem for vsechny znaky in sibenice list a v něm if
    pozice_sibenice = 0
    print (sibenice_list)
    for znak in word_guess:
        pozice_sibenice +=1
        if znak == guess_chart_value:
        sibenice_list_guess[pozice_sibenice] = guess_chart_value
    else:
        print("Netrefil jsi písmenko")
        zivoty = zivoty-1
        print(f"Zbívající počet životů:{zivoty}")
        if zivoty ==0:
            print("GEJM OUVR")
            break

    # pozice_sibenice = 0
    # try:
    #     pozice_sibenice = sibenice_list.index(guess_chart_value)
    #     print ("Ano trefil jsi písmenko")
    #     sibenice_list_guess[pozice_sibenice] = guess_chart_value
    # except ValueError:
    #     print("Netrefil jsi písmenko")
    #     zivoty = zivoty-1
    #     print(f"Zbívající počet životů:{zivoty}")
    #     if zivoty ==0:
    #         print("GEJM OUVR")
    #         break
        
        
    #print(f"Pismeno{guess_chart_value} je na {pozice_sibenice+1} pozici v sibenici")
    
    #uhlazeny vystup
    for poz in (sibenice_list_guess):
    
        print(poz,end=" ")
    print("\n")
        
# potřebuji to nějka ukončit nefunguje základní while cyklus     
else:
    print (f"uhodl jsi {word_guess}")
    print("konec hry")

    print(letters)
    print(guess_chart_value.upper())