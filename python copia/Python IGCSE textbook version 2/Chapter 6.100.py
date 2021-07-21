from tkinter import *
                            
# Task build a Tkinter CO2 wasted and saved and calculate fine

Wast_or_savedpoint = ''
fine=0

def Wasted():
    global Wast_or_savedpoint
    Wast_or_savedpoint = 'W'

def Earnt():
    global Wast_or_savedpoint
    Wast_or_savedpoint = 'E'

def Earnt_radiator():
    global Wast_or_savedpoint
    Wast_or_savedpoint = 'R'

def Wasted_radiator():
    global Wast_or_savedpoint
    Wast_or_savedpoint = 'WR'

def evulate():
    time = float(timebox.get())
    Temp = float(tempbox.get())
    Earn = Temp/time
    Addedfine=time+fine
    textbox_ans.delete(0.0, END)
    if Wast_or_savedpoint == 'E':
        textbox_ans.insert(END, time-fine)
    elif Wast_or_savedpoint == 'W':
        textbox_ans.insert(END, Earn+fine)
    elif Wast_or_savedpoint == 'WR':
        textbox_ans.insert(END, Addedfine+fine*2)
    elif Wast_or_savedpoint == 'R':
        textbox_ans.insert(END, ((Temp/time)-fine)*2)
    else:
        textbox_ans.insert(END, 'Incorrect operator')

#Build GUi

window = Tk()
window.title("CO2 calcualtor")

# Labels

Label1 = Label(window, text = 'Temp of shower/radiator').grid(row = 0, column = 1, columnspan = 2)
Label2 = Label(window, text = 'Time').grid(row=0, column = 0, sticky = W)
Label3 = Label(window, text = 'Answer').grid(row = 3, column = 0)

# 2 empty Textboxes

timebox = Entry(window, width = 10)
timebox.grid(row = 1, column = 0, columnspan = 2, padx = (0,5), sticky=W)
tempbox = Entry(window, width = 10)
tempbox.grid(row = 1, column = 1, columnspan = 2, sticky=W)

# 1 output Textbox

textbox_ans = Text(window, width = 15, height = 1, bg = 'light green')
textbox_ans.grid(row = 5, column = 0)

# Buttons

CO2_M_fine_in_shower = Button(window, text = 'CO2 +fine(shower)', width=12, command = Wasted)
CO2_M_fine_in_shower.grid(row=2, column=0)
CO2_saved_fine_in_shower = Button(window, text = 'CO2 -fine(shower)', width=12, command = Earnt)
CO2_saved_fine_in_shower.grid(row=2, column=1)
CO2_M_fine_in_radiator = Button(window, text = 'CO2 -fine(radiator)',width=12, command = Wasted_radiator)
CO2_M_fine_in_radiator.grid(row=3, column=0)
CO2_saved_fine_in_radiator = Button(window, text = 'CO2 +fine(radiator',width=12, command = Earnt_radiator)
CO2_saved_fine_in_radiator.grid(row=3, column=1)
button_equals = Button(window, text = '=',width=12, command = evulate)
button_equals.grid(row=4, column=0, columnspan= 2)

window.mainloop()
