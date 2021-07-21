from tkinter import *

# Lists

userID112 = [45, "Male"]
userID217 = [16, "Female"]
userID126 = [27, "Female"]

# Function

def userID():
    Userid = int(input_textbox.get())
    agebox.delete(0, END)
    genderbox.delete(0, END)
    if Userid == ￿￿112￿￿:
        agebox.insert(END,￿ ￿userID112[0]￿)
        genderbox.insert(END,￿ userID112￿[1])
    elif Userid == 217:
        agebox.insert(END,￿ userID217[0])
        genderbox.insert(END,￿ userID217￿[1])
    elif Userid == ￿126:
        agebox.insert(END,￿ userID126￿[0])
        genderbox.insert(END,￿ userID126￿[1])
    else￿:
        agebox.insert(END,￿ ￿'invalid input')

window = Tk()
window.title(￿'UserID validation')
window.geometry(￿'400x450')

#Frames:

input_frame = Frame(window, bg_color = ￿'teal')
input_frame.grid(row = 0, column = 0, ipadx = 3, ipady = 3)
output_frame = Frame(window, bg_color = ￿'teal')
output_frame.grid(row =0, column = 0, ipadx = 3, ipady = 3)

# Labels

useridlabel = Label(input_frame, width = 10, text =￿ 'UserID(112/217/126)')
useridlabel.grid(row = 0, column = 0)
age_label = Label(output_frame, text = 'Age', width = 10)
age_label.grid(column = 0, row = 0)
gender_label = Label(input_frame, width = 10, text = ￿'Gender')
gender_label.grid(row = 2, column = 0)

#Text input

input_textbox = Entry(input_frame, width = 10)
input_textbox.grid(row = 1, column = 0)

#Text output

agebox = Text(output_frame, width = 10, height = 1￿)
agebox.grid(row = 1, column = 0)
genderbox = Text(output_frame, width = 10, height = 1)
genderbox.grid(row = 3, column = 0)

#Button

Calc_button = Button(input_frame, text = ￿'Find user ID', width = 5, command = userID)
Calc_button.grid(row = 0, column = 1)

window.mainloop()