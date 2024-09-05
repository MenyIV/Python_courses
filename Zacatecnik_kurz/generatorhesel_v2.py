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


# print(pocPismen)
# print(pocCisel)
# print(pocZnaku)

#if pocPismen != 0:
for pismena in range (int(pocPismen)):
        pismena_list.append(random.choice(letters))
        #print (pismena_list)
#if pocCisel != 0:
for cisla in range (int(pocCisel)):
        cisla_list.append(random.choice(numbers))
        
#if pocZnaku != 0:1
for znaky in range (int(pocZnaku)):
        znaky_list.append(random.choice(special_char))
        

# print (pismena_list)
# print (cisla_list)
# print (znaky_list)


heslo_list = pismena_list+cisla_list+znaky_list

# print(heslo_list)

for znakhesla in heslo_list:
    print(znakhesla,end="")
    
print("")  

for michacka in range (3):
    random.shuffle(heslo_list) 
    for znakhesla in heslo_list:
        print(znakhesla,end="")  
    print("")  
