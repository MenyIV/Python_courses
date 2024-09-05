
#taky funguje
# def better_name (first_name , second_name):
#     full_name = first_name + " " + second_name
#     return full_name.title()


def better_name(first_name,second_name):
    first_name = first_name.capitalize()
    second_name = second_name.capitalize()
    return f"{first_name} {second_name}"


result = better_name("jan","suchy")
print(result)