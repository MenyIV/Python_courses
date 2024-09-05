# fizz buzz
# pokud je dělitelné 3 fizz pokud 5 buzz pokud oběma tak fizz buzz
fizz = 3
buzz = 5

for cislo in range(1,101):
    hlaska1 =("")
    hlaska2 =("")
    hlaska3 = str(cislo)
    
    #print (cislo)
    if cislo % fizz == 0:
        hlaska1 = ("fizz")
        hlaska3 = str("")
        #print ("je to /3")
    
    if cislo % buzz == 0:
        hlaska2 = ("buzz")
        hlaska3 = str("")
        #print ("je to /5")
 #   elif:
 #       hlaska3 = str(cislo)
        #print ("je to cislo")
    print (f"dítě říká {hlaska1}{hlaska2}{hlaska3}")
