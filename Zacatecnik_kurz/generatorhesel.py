#kolik písmen má mít heslo:
#kolik čísel
#kolik speciálních znaků

#na konec to prohrkat ať je to spřeházené ??
import math
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = [ '%', '#', '$', '!', '&', '(', ')', '*', '+', '?']
password = []
pismena_list = []
cisla_list = []
znaky_list = []

pocPismen = input("zadej požadovaný počet písmen:")
pocCisel = input("zadej požadovaný počet čísel:")
pocZnaku = input("zadej požadovaný počet znaků:")


print(pocPismen)
print(pocCisel)
print(pocZnaku)

#if pocPismen != 0:
for pismena in range (0,int(pocPismen)-1):
        #tohle nebude fungovat spolehlivě kvůli tomuhle řádku
        rand = (math.ceil(random.random()*len(letters)))
        pismeno = letters[int(rand)]
        pismena_list.append(pismeno)
        #print (pismena_list)
        
#if pocCisel != 0:
for cisla in range (0,int(pocCisel)-1):
        rand = (math.ceil(random.random()*len(numbers)))
        cisla = numbers[int(rand)]
        cisla_list.append(cisla)
        
#if pocZnaku != 0:
for znaky in range (0,int(pocZnaku)-1):
        rand = (math.ceil(random.random()*len(special_char)))
        znaky = special_char[int(rand)]
        znaky_list.append(znaky)
        

print (pismena_list)
print (cisla_list)
print (znaky_list)

heslo_list = pismena_list+cisla_list+znaky_list

print(heslo_list)

#rand = (math.ceil(random.random()*6))
#pismeno=letters[int(rand)]
#print (pismeno)


#vypsání hesla

for znakhesla in heslo_list:

    print(znakhesla,end="")

    
print("Míchám heslo")  
random.shuffle(heslo_list) 

for znakhesla in heslo_list:
    print(znakhesla,end="")
    
print("")  