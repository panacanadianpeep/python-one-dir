# calculator gui

from tkinter import *

# Functions goes here
def change_text():
    my_label.config(text=gender.get())

# create main tkinter window
window = Tk()
window.title('My application')

# add an empty tkinter label widget and place at grid lock
my_label = Label(window, width=25, height=1, text='')
my_label.grid(row=0, column=0)

# add an tkinter button widget, place in a grid layout and attach to change text button

my_button = Button(window, text='Submit', width=10, command=change_text)
my_button.grid(row=1, column=0)

# Create a Tkinter string variable object for the radio buttons

gender = StringVar()

# add 2 radio buttons use optional sticky argument to align left

radio1 = Radiobutton(window, text='Female', variable=gender, value='female')
radio1.grid(row=2, column=0, sticky=W)
radio1.select() # free selects radio button for user
radio2 = Radiobutton(window, text='Male', variable=gender, value='male')
radio2.grid(row=3, column=0, sticky=W)

window.mainloop()