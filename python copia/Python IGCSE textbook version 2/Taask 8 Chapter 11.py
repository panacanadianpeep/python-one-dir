from tkinter import *

UserID112 = [45, "Male"]
UserID217 = [16, "Female"]
UserID126 = [27, "Female"]

UserID = int(input("Input your user ID(User ID = 112, 217, 126)"))

while UserID != 112 or UserID != 217 or UserID != 126:
    if UserID == 112:
        print("Age is equal to", UserID112[0], "and gender is equal to", UserID112[1])
    elif UserID == 126:
        print("Age is equal to", UserID126[0], "and gender is equal to", UserID126[1])
    elif UserID == 217:
        print("Age is equal to", UserID217[0], "and gender is equal to", UserID217[1])
    elif UserID == 1:
        break
    else:
        print("Wrong input")
    UserID = int(input("Input your user ID(User ID = 112, 217, 126, 1(terminate program))"))