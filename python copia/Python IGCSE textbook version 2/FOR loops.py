import time

def user_input(num, pfw):
    while window == True:
        if 1000 > num < 1500:
            print("unvalid input")
            num = int(input("What is your user ID"))
        elif len(pfw) < 6:
            print("Invalid user input")
            pfw = input("Password")
        else:
            print("Loading")
            wndow = False
            break

window = True

while window == True:
    num = int(input("What is your user ID"))
    pfw = input("Password")
    user_input(num, pfw)
    if num > 999 and 1500 < num:
        if len(pfw) < 6:
            window = False
    else:
        window = False

print("I love you")
