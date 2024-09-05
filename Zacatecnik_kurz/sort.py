seznam_dict= {
    "raketa":6,
    "trubice":7,
    "okno":4,
    "monitor":7,
    "kolo":4,
    "stativ":6,
    "kamera":6,
    "lzice":5,
    "papirek":7,    
}

sorted_dict={}


worksheet = []

i=0 #startovací pozice v seznamu pro sort

#jak to setřídit
#asi bych si to nejdřív měl hodit do listu atˇse v tom můžu pohynbovat
#vezmu si první a porovnám ho s následujícím když je vjětší tak ok když menší tak ho hodím nakonec a znovu

# převedení na list
for each in seznam_dict:
    worksheet.append(each)
    print(each)
    
while i != int(len(seznam_dict)):
    print(i)
    print(seznam_dict[worksheet[i]]) 
    print(seznam_dict[worksheet[i+1]])     
    if seznam_dict[worksheet[i]] > seznam_dict[worksheet[(i+1)]]:
        i+=1
    else:
        # pokud ne tak vezmne to druhý a hodí to na první místo a přehází do sorted dict nakonec přepíše sorted do seznamdict
        #print(worksheet[i+1])
        presun = (worksheet[i+1])
        worksheet.remove(worksheet[i+1])
        worksheet.insert(0,presun)
        i=0
        for mem in worksheet:
            #print(seznam_dict[mem])
            sorted_dict=+(seznam_dict[mem])
        #print (worksheet)
print(seznam_dict)
print(sorted_dict) 
    
    
    
# potřebuju zjistit jak přesypat hoddnoty jednoho dictu do druhého podle pořadíá v seznamu