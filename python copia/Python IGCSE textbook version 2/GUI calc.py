from tkinter import *

# initialise tglobal variable

operator = ''

# functions

def set_A():
    global operator
    operator = 'A'

def set_S():
    global operator
    operator = 'S'

def set_M():
    global operator
    operator = 'M'

def set_D():
    global operator
    operator = 'D'

def evulate():
    number1 = float(textbox1.get())
    number2 = float(textbox2.get())
    textbox_ans.delete(0.0,  END)
    if operator == 'A':
        textbox_ans.insert(END, number1 + number2)
    elif operator == 'S':
        textbox_ans.insert(END, number1 - number2)
    elif operator == 'M':
        textbox_ans.insert(END, number1 * number2)
    elif operator == 'D':
        textbox_ans.insert(END, number1 / number2)
    else:
        textbox_ans.insert(END, 'Incorrect operator')

# Build the GUI:

window = Tk()
window.title("Calculator")

# Create labels

Label1 = Label(window, text = 'number 1').grid(row = 0, column = 0, columnspan = 2)
Label2 = Label(window, text = 'number 2').grid(row = 0, column = 2, sticky = W)
Label3 = Label(window, text = 'Answer').grid(row=3, column = 2)

# Creat 2 empty textboxes

textbox1 = Entry(window, width=10)
textbox1.grid(row = 1, column = 0, columnspan = 2, padx = (0,5), sticky=W)
textbox2 = Entry(window, width = 10)
textbox2.grid(row = 1, column = 2, sticky=W)

# Create a text output box
textbox_ans = Text(window, width = 14, height = 1, bg = 'light green')
textbox_ans.grid(row = 4, column=2, sticky = W)

# add the operator button

button_add = Button(window, text = '+', width=3, command = set_A)
button_add.grid(row=2, column=0)
button_subtract = Button(window, text = '-', width=3, command = set_S)
button_subtract.grid(row=2, column=1)
button_multiply = Button(window, text = '*',width=3, command = set_M)
button_multiply.grid(row=3, column=0)
button_divide = Button(window, text = '/',width=3, command = set_D)
button_divide.grid(row=3, column=1)
button_equals = Button(window, text = '=',width=6, command = evulate)
button_equals.grid(row=4, column=0, columnspan= 2)

window.mainloop()