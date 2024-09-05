import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = [ '%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

letters_list = []

for pismeno in range (0, len(letters)):
    nahodne_cislo = random.randrange(0,len(letters))
    #print(letters[nahodne_cislo])
    letters_list.append(letters[nahodne_cislo])
    #print(letters_list)
    
print(len(letters))
print(len(letters_list))

print(letters_list)

for heslo in range (0, len(letters_list)):
    rand1 = random.randint(0,len(letters_list)-1)
    rand2 = random.randint(0,len(letters_list)-1)

    hold = letters_list[rand1]
    letters_list[rand1] = letters_list[rand2]
    letters_list[rand2] = hold
    
print("Zamichany seznam")
print(letters_list)
for znak in letters_list:
    #heslo += (letters_list[index])
    print(znak,end="") 
    
print(heslo)