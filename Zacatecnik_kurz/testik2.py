vstup_list = [' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9']
vystup_list = []
each2=print(input("Zadej cislo"))
print(each2)
for each in vstup_list:
    vystup_list.append(each[1])
    pozice = vstup_list.index(each)
    print(pozice)
print(vstup_list)
print(vystup_list)
