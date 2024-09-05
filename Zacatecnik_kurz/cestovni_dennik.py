# zadej Country
# zadej navstineva mesta
# zadej pocet navstev

#nakonec to pridej do deniku


travel_diary =[
    {"Country":"Spain",
     "Navstivena mesta":["Madrid","Leon","Valencie"],
     "navstevy":5
     },
    {"Country":"France",
     "Navstivena mesta":["Paříž","Nice"],
     "navstevy":10},
    ]
def vlozeni(country,mesto,navstevy):
    mesto.remove("")
    travel_diary.append({"Country":country,"Navstivena mesta":mesto,"navstevy":navstevy})
    
next = "A"
mesto = []
zadej_mesto = "i"

print (travel_diary[1]["Navstivena mesta"][1])


country = input("Zadej stát\n")
while zadej_mesto != "":
    zadej_mesto= input("Zadej město\n")
    mesto.append(zadej_mesto)

navstevy = input("Zadej pocet návstev\n")

vlozeni(country,mesto,navstevy)

print(travel_diary)

