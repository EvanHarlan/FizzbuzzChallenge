# Write a python program that numbers 1 - 100
# Multiples of 3 - print "Fizz"
# Multiples of 5 - print "Buzz"
# Multiples of 3 & 5 - print "FizzBuzz"
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)