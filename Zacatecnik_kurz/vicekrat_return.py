def better_name (first_name , second_name):
    if first_name == "" or second_name == "":
        return "Není zadáno jméno"
    full_name = first_name + " " + second_name
    return full_name.title()


result = better_name(input("Vaše jméno"), input("Vaše příjmení"))
print(result)