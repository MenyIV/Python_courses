set1 = ["00","01🌅","02🏪","03🌅"]
set2 = ["10","11🌅","12🏪","13🌅"]
set3 = ["20","21🌅","22🏪","23🌅"]
set4 = ["30","31🌅","32🏪","33🌅"]

all_sets = [set1,set2,set3,set4]

position = input("Zadej souřadnice 0-3,0-3")

print (f"Zvolené souřadnice jsou: {position}")
#print (all_sets)
#print (f"{set1}\n{set2}\n{set3}\n{set4}\n")

#line = int(position[0])
#row = int(position [-1])

#print (f"row{row}")
#print (f"line{line}")

#all_sets = (all_sets[line][row])
all_sets[int(position[0])][int(position [-1])] = "X"

#all_sets = (all_sets[[position[1]],[position[-1]]])


#print (all_sets)
print (f"{set1}\n{set2}\n{set3}\n{set4}\n")