# Import

from tkinter import *
import random

# Function

def speeding_ticket():

    distance = int(distance_box.get())

    time = int(time_box.get())

    max_speeding = random.randrange(40, 100)

    fine = (max_speeding-(distance / time))*1.011

    output_textbox.delete(0.0, END)

    output_textbox.insert(END, fine)

# Intisalise Tkinter

window = Tk()
window.title('Speed ticket cost')

# Configure background color and size

window.configure(background = 'light blue')
window.geometry('450x500')

# Add labels

distance_label = Label(window, width = 15, text = 'Distance', bg = 'orange')
distance_label.grid(row = 0, column = 0)
time_label = Label(window, width = 15, text = 'Time?:', bg = 'orange')
time_label.grid(row = 0, column = 1)

# Input Textbox

distance_box = Entry(window, width = 15, bg = 'Orange')
distance_box.grid(row = 1, column = 0)
time_box = Entry(window, width = 15, bg = 'Orange')
time_box.grid(column = 1, row = 1)

# Output textbox

output_textbox = Text(window, width = 25, bg= 'Yellow', height = 1)
output_textbox.grid(row = 2, column = 1)

# Button

Speed_button = Button(window, width = 10, command = speeding_ticket, text = 'Calculate fine')
Speed_button.grid(row = 0, column = 2)

window.mainloop()