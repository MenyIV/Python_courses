import random

seznam_list = ["Ron","Hermiona","Harry","Hagrid"] 
count = 5
counter = 1

print("Hádej jméno z filmu HarryPotter\n")
odhad = ""

vyber=seznam_list[random.randint(0,len(seznam_list)-1)]


while vyber != odhad and count != counter:
    print(f"pokus: {counter}")
    odhad = input(print("Napiš jméno:\n"))
    counter +=1

if count != counter:   
    print(f"Uhodl jsi {odhad}\n")
else:
    print(f"prohrál {odhad}\n")

