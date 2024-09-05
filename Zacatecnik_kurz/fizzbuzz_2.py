# fizz buzz
# pokud je dělitelné 3 fizz pokud 5 buzz pokud oběma tak fizz buzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print (number)
        