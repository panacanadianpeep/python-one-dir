from tkinter import *

def multiply():
    number = int(Input_textbox.get())

    textbox_output.delete(0.0, END)

    for counter in range(1,11):
        multiple = str(number * counter) + '\n'
        textbox_output.insert(END, multiple)

# Build the GUI

window = Tk()
window.title("Multpliers of a number")

# Set size and other stuff

window.geometry('350x700')
window.configure(background='linen')

# Labels

Number_label = Label(window, height = 1, width = 5,text = 'Number:')
Number_label.grid(row=0, column=0)
Output_label = Label(window, height = 1, width = 5, text = 'Output:')
Output_label.grid(row=2, column=0)

# Textboxes

Input_textbox = Entry(window, width=6, bg='Yellow')
Input_textbox.grid(row=1, column = 0)

# output textbox

textbox_output = Text(window, height = 12, width=6)
textbox_output.grid(row=3, column= 0)

multiply_button = Button(window, text = 'Get Multiples', width = 10, command = multiply)
multiply_button.grid(row = 0, column = 1)

window.mainloop()