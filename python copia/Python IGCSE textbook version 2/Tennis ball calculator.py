from tkinter import *

# Use function

def balls():

    number_of_balls = int(input_textbox.get())

    output_textbox.delete(0.0, END)

    cost_of_balls = number_of_balls*1.5-((0.0001 * number_of_balls)/50)

    output_textbox.insert(END, cost_of_balls)

# initalise tkinter:

window = Tk()
window.title('Tennis ball cost calculator')

# Background and color:

window.geometry('350x300')
window.configure(background = 'light blue')

# Labels:

Input_label = Label(window, width = 20, text = 'number of balls')
Input_label.grid(row = 0, column = 0)
output_label = Label(window, width = 20, text = 'Cost of tennis balls')
output_label.grid(row = 2, column = 0)

# Textboxes:

input_textbox = Entry(window, width=20, bg = 'light green')
input_textbox.grid(row  = 1, column = 0)
output_textbox = Text(window, width = 20, height = 1)
output_textbox.grid(row = 3, column = 0)

# Button:

Calc_button = Button(window, width = 6, bg = 'yellow', text = 'Calculate', command = balls)
Calc_button.grid(row = 1, column = 1)

window.mainloop()