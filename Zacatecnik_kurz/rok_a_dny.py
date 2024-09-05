# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#
#dělitelný čyřmi 
#nedělitelný 100
#dělitelný 400
#ověřit zda je v listu

# uživatel zadá měsíc a bude vypsán počet dní v měsíci
#pozor pokud je přestupný tak únor má 29
# napsat na to funkci která vráttí výsledek

prestupny = ()
x=0

days_in_month= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def month_lenght(mesic,x):
    # print (mesic)
    # print(x)
    if mesic == 2 and x == 1:  #toto zdá se že nefachá
        print("prestupny unor má 29 dní")
        return
    else:
        print(f"{days_in_month[mesic]}")
        return




def prestup (rok):
    if rok % 4 == 0:
        if rok % 100 != 0:
            x=1
            print (f"Rok {rok} je přestupným rokem")
            return x
        else:
            if rok % 400 == 0:
                x=1
                print (f"Rok {rok} je přestupným rokem")
                return x
            else:
                
                print (f"Rok {rok} není přestupným rokem")
        
    
    else:
        print (f"Rok {rok} není přestupným rokem")
   
rok = int(input("zadej rok\n"))
mesic = int(input("Zadej číslo měsíce:"))

x=prestup(rok)
month_lenght(mesic,x)