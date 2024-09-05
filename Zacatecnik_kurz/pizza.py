# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#velikost pizzy S100 M150 L200
#feferoni ano ne S+20 ML+30
#Syra ano ne +15

pizza = input("Jakou velikost pizzy chceš? s;m;l")
feferoni = input("Přejete si feferoni a/n")
syr = input("Sejra? a/n")
cena = 0


if pizza == "s":
    cena +=150
    if feferoni == "a":
        cena +=20
    
elif pizza == "m":
    cena +=200
    if feferoni == "a":
        cena +=30

elif pizza == "l":
    cena +=250
    if feferoni == "a":
        cena +=30
else:
    print("Takovou pizzu nemám")

if syr == "a":
    cena +=15
else:
    print("Jeden FIT kousek")
print(f"výsledná cena je {round(cena,2)} Kč")