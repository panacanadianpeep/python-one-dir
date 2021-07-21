#Functions
def array_input(num):
    for i in range(0, 12):
        multiples[i] = num * (i+1)

def array_display():
    for i in range(0,12):
        print(multiples[i])

## Main
# Declare an array with spaces for 12 data items

multiples = [None]*12

# Use triple quotes to make menu formation easy

action = int(input('''Choose from:

1. Input
2. Display
3. Exit

[1, 2, or 3]?'''))

while action == 1 or action == 2:
    if action == 1:
        multiple = int(input("Input a whole number"))
        array_input(multiple)
    elif action == 2:
        array_display()
    else:
        break
    action = int(input('\n choose 1, 2 or 3'))