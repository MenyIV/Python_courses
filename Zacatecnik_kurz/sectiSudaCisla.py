#secti suda cisla od 1 do 100
# pro lichá nerovná se !=

import math
rozsah_start = 1
rozsah_cil = 100
cislo = rozsah_start
soucet = 0

#zda je sude
for cislo in range (rozsah_start,rozsah_cil):
    cislo = (cislo + 1)
    podil = cislo /2
    #print (podil)
    if cislo % 2 == 0:
    #if isinstance(podil,int):
        soucet = soucet + cislo
    else:
        print (f"{cislo} není sudé")
        
print (f"součet sudých čísel v rozshau {rozsah_start} až {rozsah_cil} je {soucet}")