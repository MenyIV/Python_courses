#tuple - nelze změnit
my_tuple = (1,2,3)


#list
my_list= [1,2,3]

print(my_tuple[1])
print(my_list[1])

# my_tuple[1] = 0  -- vyhazuje chybu
my_list[1] = 0

print(my_tuple[1]) 
print(my_list[1])

change_tuple_to_list = list(my_tuple) #převedení neměnného tuplu na změnitelný list
change_tuple_to_list[1] = 0

print (change_tuple_to_list[1])