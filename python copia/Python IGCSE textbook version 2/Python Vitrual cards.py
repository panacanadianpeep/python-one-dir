import random

while True:
    number = random.randrange(0,13)
    if number == 0:
        print("Ace")
    elif 2 < number < 10:
        print(number)
    elif number == 11:
        print("jack")
    elif number == 12:
        print("Queen")
    elif number == 1:
        print("King")
    ready = input("Next")