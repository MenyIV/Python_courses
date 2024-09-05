letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

zasifrovaneslovo = []

#program který šifrouje a dešifruje zprávy Cesarovy šifry.
#Posune znaky v abecedě dle daného počtu posunutí.

#znaky které nejsou v řetězci       -OK
#ochrana přetečení letters listu +  -OK
#ošetření mezer                     -OK
#chceš šifrovat nebo dešifrovat?    -OK 
#posun *-1 - posun do mínusu s přetečením pole -??? netestováno

#Testovací zpráva:
# Toto je zpráva zeheslovaná cesarovou šifrou s posunem o 10 znaků.

vstup = input("Zadej řeťezec znaků které chceš šifrovat:")
posun = int(input("Zadej číslo klíče k šifře:"))

smer = int(input("Pokud si přeješ šifrovat zadej [1] dešifrovat zadej [0]"))
print (f"{smer}")
#sifrovani desifrovani
if smer == 1:
    posun = posun
if smer == 0:
    posun = posun*-1

    
vstup_list =[]
vstup_dellist =[]

print (f"Šifruji {vstup}, klíčem {posun}")

delkalistu = int((len(letters)))
#print(f"základ šifry je {delkalistu}")

#neplatné znaky
neplatne_znaky = []

#rozebere string na list
for znak in vstup:
    vstup_list.append(znak)
#print(f"Vstupní list:{vstup_list}")
#najde a vyhází neplatné znaky
for znak in vstup:
    #print(f"hodnotím znak{znak}")
    if znak not in letters and znak != " ":
        neplatne_znaky.append(znak)
        vstup_list.remove(znak)
        
                 
#opět upraví vstup pro šifrovací smyčku a oznámí které znaky byly vyřazeny     
vstup = "".join(vstup_list)
print(f"Nové znení zprávy:{vstup}")
print(f"Z sifrovane zprávy byly vyřazeny tyto znaky: {neplatne_znaky}")


#šifrovaací smyčka
for pismeno in vstup:
    if pismeno != " ":
        pozpismena=letters.index(pismeno)
        #print(f"pozice{pozpismena}")
        index = int(pozpismena) + int(posun)
        if index > delkalistu:
            index=posun%delkalistu
            #index=index-1
            #print(f"posun po dělení je{index}")
        zasifrovaneslovo.append(letters[index])
    else:
        zasifrovaneslovo.append(" ")           
    #print(f"vypisu pismeno z pozice:{index}")
    

#print(f"Sifra je: {zasifrovaneslovo}")
# #Vypsání pěkného hesla
print("Vaše zašifrovaná zpráva:\n")
print("".join(zasifrovaneslovo))
print("\n")
    
