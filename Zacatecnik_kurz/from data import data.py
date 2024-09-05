from data import data
import random

# vypíše ten má tolik foloweru 
# a zeptá se kolik myslíš že má tenhle vín nebo míň?

# na začátku vybereme jedno libovolného
# funkce pro výběr jednoho random údaje
# funkce pro porovnání má víc má míň


#tuningy
# udělat tak aby se nemohly potkat dva stejné


delka_dat = len(data)-1
print(delka_dat)
print(data[1])
print(data[random.randint(0,delka_dat)])
