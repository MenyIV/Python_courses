
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
#            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['0', '1', '2', '3', '4','5']
# special_char = [ '%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

import time
import random

print(len(letters))
letters_frame = []

letters_frame.extend(letters)

counter = 0
random.shuffle(letters) 

while letters_frame != letters:
    counter +=1
    random.shuffle(letters) 
    #time.sleep (1)
    
    # for znakhesla in letters_mix:
    print(letters_frame)
    print(letters,end="")
    print(counter)