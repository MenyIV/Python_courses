# nejde

seznam_dict= {
    "raketa":6,
    "trubice":7,
    "okno":4,
    "monitor":7,
    "kolo":4,
    "stativ":6,
    "kamera":8,
    "lzice":9,
    "papirek":7,    
}

sorted_list=[]
sorted_dict={}


worksheet = []

i=0 #startovací pozice v seznamu pro sort

# projede worksheet najde nejvyšší a vrazí ho do sorted list
# a vyndá ho z worksheet

# převedení na list
for each in seznam_dict:
    worksheet.append(each)

print(f"Seznam prvním průchodem třízení {worksheet}")    
while len(worksheet) == 0:
    for nazev in worksheet:
        
        if seznam_dict[nazev] > i:
            
            i=seznam_dict[nazev]
            zapis=(nazev)
            worksheet.remove(nazev)
            print(worksheet)
            print(zapis)
            print (i)
            sorted_list.append(zapis)
            print(sorted_list)

    
    
    
print(f"Seznam po třízení jednom průchodu třízení {sorted_list}")