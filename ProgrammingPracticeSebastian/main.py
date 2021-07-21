"""
Exercise 1:
Create an algorithm that will ask the user for two numbers and print their sum.
"""

number1 = int(input("Input first number to add"))
number2 = int(input("Input second number to add"))
sum = number1 + number2
print(sum)

"""
Exercise 2:
Create an algorithm that asks the user for a number, and then adds all the numbers that come before it starting at 1.

Example: User types 5, the printed answer should be 5+4+3+2+1 which is 15. The program should print 15.
"""

number = int(input("What number do you want to print out?"))

sum = 0

for i in range(number + 1):
  sum = sum + i

print(sum)

"""
Exercise 3:
Prompt a user for a number. Then divide that number into the variable a and print the variable a.
"""

numberToDivide = int(input("Number to divide?"))
a = 6 # can't change
a = a / numberToDivide
print(a) # can't change

"""
Exercise 4:
Create an algorithm that will ask for a number from the user, and use a for loop to add 3 to a sum the number of times that the user entered.

Example:
Enter a number please: 5
Behind the scenes: sum with three more, then three more, #hen three more.. until we reach 5 times.
Result: 15
"""

number_input = int(input("Enter a number please: "))

sum = 0

for i in range(number_input):
  sum = sum + 3

print("Result: " + str(sum))

"""
Exercise 5
Create an algorithm that asks the user for a number and print the message: "You need a better for loop" that number of times on a new line each time.
"""

number = int(input("number"))

for i in range(number):
  print("You need a better for loop")