#Nesting

#list v dictionary
mesta = {
    "Španělsko":"Madrid",
    "Francie":"Paříž",
    "Senegal":"Dakar"
}

# denik={
#     "Španělsko":["Madrid","Leon","Valencie"],
#     "Francie":["Paříž","Nice"]
# }

# print(denik)
# print(denik["Francie"])
# print(denik["Španělsko"][1])

#dictionary v dictionary


# denik={
#     "Španělsko":{"Navstivena mesta":["Madrid","Leon","Valencie"],
#                  "navstevy":5},
#     "Francie":{"Navstivena mesta":["Paříž","Nice"],
#                "navstevy":10}
# }

# print (denik["Francie"]["navstevy"])
# print (denik["Francie"]["Navstivena mesta"][0])


#dictionary v listu

travel_diary =[
    {"Country":"Spain",
     "Navstivena mesta":["Madrid","Leon","Valencie"],
     "navstevy":5
     },
    {"Country":"France",
     "Navstivena mesta":["Paříž","Nice"],
     "navstevy":10},
    {}
    ]

print (travel_diary[1]["Navstivena mesta"][1])