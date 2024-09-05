#Globální proměnná

def test():
    global my_jmeno
    my_jmeno = "Harry"
    print(my_jmeno)
    
    
test()
print(my_jmeno)