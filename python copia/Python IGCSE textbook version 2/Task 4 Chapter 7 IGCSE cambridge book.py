from tkinter import *

def prime():

    # Get contents of textbox input
    modulus_counter = 0

    # Clear output textbox
    number = int(textbox_input.get())

    # Run algorithm
    textbox_output.delete(0.0, END)

    for counter in range(2, number):
        modulus = number % counter
        if modulus == 0:
            modulus_counter = modulus_counter + 1

    if modulus_counter == 0:
        textbox_output.insert(END, "prime number")

    else:
        textbox_output.insert(END, "Not a prime number")

# Initialise GUI

window = Tk()
window.title('Prime number checker')

# Background and size

window.geometry('150x350')
window.configure(background = 'yellow')

# Create Labels

input_label = Label(window, width = 20, text = 'Input your chosen number')
input_label.grid(row = 0, column = 0)
output_label = Label(window, width = 20, text = 'Prime/Not prime output')
output_label.grid(row = 2, column = 0)

# Create input textbox
textbox_input = Entry(window, width = 15)
textbox_input.grid(row = 1, column = 0)

# Output textbox

textbox_output = Text(window, width = 20, height = 1)
textbox_output.grid(row = 3, column = 0)

Button = Button(window, width = 10, text = 'Run', command = prime)
Button.grid(row = 1, column = 1)

window.mainloop()