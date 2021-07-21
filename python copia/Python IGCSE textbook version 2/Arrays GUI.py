from tkinter import *

# Declare list globally to allow both subroutines

task = [None] * 4

# Functions

def input_data():

    # collect values from Entry box

    data_item = int(tbox1.get())
    index = int(tbox2.get())

    # insert ne value into array:

    task[index] = data_item

def output_data():

    # Collect index required
    index = int(tbox3.get())

    # Clear output text box and display data

    tbox4.delete(0, END)

    tbox4.insert(END, task[index])

# BUild the GUI
# padding is added to some widgets
# ipadx add internal padding to left and right
# padx adds external padding to left and right
window = Tk()
window.title('My application')
bg_colour = 'linen'

# Create two frames

input_frame = Frame(window, bg = bg_colour)
input_frame.grid(row = 0, column = 0, ipadx = 5, ipady = 5)
output_frame = Frame(window, bg = bg_colour)
output_frame.grid(row = 0, column = 1, ipadx = 5, ipady = 5)

# Create the labels

input_label1 = Label(input_frame, text = 'Data Item to Add', bg= bg_colour)
input_label1.grid(row = 1, column = 0, sticky = W)
input_label2 = Label(input_frame, text = 'Index to be Used', bg = bg_colour)
input_label2.grid(row = 2, column = 0, sticky = W)
output_label1 = Label(output_frame, text = 'Index to Display', bg = bg_colour)
output_label1.grid(row = 1, column = 0, sticky = W)
output_label2 = Label(output_frame, text = 'Value in Index', bg = bg_colour)
output_label2.grid(row = 2, column = 0, sticky = W)

#Create the buttons

inputButton = Button(input_frame, text = 'Input', command = input_data, width = 24)
inputButton.grid(row = 0, column  = 0, columnspan = 2, padx = 5, pady = 5)
outputButton = Button(output_frame, text='Output', command = output_data, width = 24)
outputButton.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

#Textbox

tbox1 = Entry(input_frame, width = 10)
tbox1.grid(row = 1, column = 1)
tbox2 = Entry(input_frame, width = 10)
tbox2.grid(row = 2, column = 1)
tbox3 = Entry(output_frame, width = 10)
tbox3.grid(row = 1, column = 1)
tbox4 = Entry(output_frame, width = 10)
tbox4.grid(row = 2, column = 1)

window.mainloop()