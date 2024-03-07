#-----------------------------#
#                             #
#       FizzBuzz Program      #
#                             #
#-----------------------------#

# For loop used to print numbers from 1 - 100
for number in range(1, 101):
    # If the number is divisible by 15 (3 & 5) - print "FizzBuzz"
    if number % 15 == 0:
        print("FizzBuzz")
    # Else if the number is ONLY divisible by 3 - print "Fizz"
    elif number % 3 == 0:
        print("Fizz")
    # Else if the number is ONLY divisible by 5 - print "Buzz"
    elif number % 5 == 0:
        print("Buzz")
    # Else print the number if it does not meet any above conditions
    else:
        print(number)