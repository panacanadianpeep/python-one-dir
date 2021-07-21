# hello-gui
from tkinter import *

#set

operator = ''

answer=number1+number2

# function called by clicking on my window
def change_text():
    my_label.config(number=answer)

# create main tkinter window
window = Tk()
window.title('My application')

# Add an empty tkinter window

my_label = Label(window, width=25, height=2, text='')
my_label.grid(row=0, column=0)

# add a tknter butoon wudgetm place it in the grid layout and attach change_text function
my_button = Button(window, text='Say Hi', width=10, command=change_text())
my_button.grid(row=1, column=0)

window.mainloop()