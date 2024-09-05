# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#
#dělitelný čyřmi 
#nedělitelný 100
#   dělitelný 400
#ověřit zda je v listu

rok = int(input("zadej rok\n"))

if rok % 4 == 0:
    if rok % 100 != 0:
        print (f"Rok {rok} je přestupným rokem")
    else:
        if rok % 400 == 0:
            print (f"Rok {rok} je přestupným rokem")
        else:
            print (f"Rok {rok} není přestupným rokem")
        
    
else:
    print (f"Rok {rok} není přestupným rokem")