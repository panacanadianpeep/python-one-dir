number = input("Input number")

# program continues=
while True:
    try:
        int(number)
        break
    except:
        number = input("Error: Please input number")
