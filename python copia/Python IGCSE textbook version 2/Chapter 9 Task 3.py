from tkinter import *

# Function

def validate():

    number = int(input_textbox.get())

    output_textbox.delete(0.0, END)

    if number > 1000 or number < 0:
        output_textbox.insert(END, 'ERROR')
    else:
        output_textbox.insert(END, 'Welcome to the club')

# Initialise Tkinter module

window = Tk()
window.title('Guard Club Validation')

#Background and size

window.geometry('200x300')
window.configure(background = 'light blue')

# Labels

input_label = Label(window, width=20, text = 'Number to the club')
input_label.grid(row=0, column = 0)
output_label = Label(window, width=20, text = 'You validated?')
output_label.grid(row = 2, column = 0)

# Input entry textbox

input_textbox = Entry(window, width=20)
input_textbox.grid(row = 1, column = 0)

# Output entry textbox

output_textbox = Text(width = 20, height = 1)
output_textbox.grid(row = 3, column=0)

#Button

Validate_button = Button(window, width = 5, text = 'Validate your number', command = validate)
Validate_button.grid(column=1, row = 1)
window.mainloop()