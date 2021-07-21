from tkinter import *

# Functions

def matcher():

    points = 0

    main_hobby = float(main_hobby_dropddown())

    if main_hobby == 'Cooking':
        points += 1
    elif main_hobby == 'Football':
        points += 2
    elif main_hobby == 'Fishing':
        points += 1.5
    elif main_hobby == 'Hunting':
        points += 3

    faviorite_genre = float(main_hobby.get)

    if faviorite_genre == 'Action':
        points += 1
    elif faviorite_genre == 'Drama':
        points += 2
    elif faviorite_genre == 'Horror':
        points += 1.5
    elif faviorite_genre == 'Sicence Fiction':
        points += 3

    Age = int(Agebox.get())

    if Age > 13:
        points = points - 30
    elif 13 < Age < 18:
        points = points + 1
    elif 18 < Age < 30:
        points = points + 2
    elif 30 < Age < 42:
        points = points + 2.5
    elif Age > 42:
        points = points + 3

    if points < 0:
        output_textbox.insert(END, 'You are too young to have a girfriend')
    elif 0 < points < 3:
        output_textbox.insert(END, 'Linda, a doctor from NYC, has a 90% chance of a succesful relaationship')
    elif 3.1 < points < 4.5:
        output_textbox.insert(END, 'Marie, a singer from LA, has a 91% chance of a succesful relationship')
    elif 4.6 < points < 7:
        output_textbox.insert(END, 'Sam, a accountant from LA, has a 88% chance of a succesful relationship')
    elif 7 < points < 9:
        output_textbox.insert(END, 'Pete has a 95% chance of a successful relationship')
    else:
        output_textbox.insert(END, 'ERROR')


# Initalise Tkinter

window = Tk()
window.title('date matcher')

# Customise window

window.geometry('550x500')
window.configure(background = 'gold')

# Labels

main_hobby_label = Label(window, width = 15, text = 'Main Hobby', bg = 'Light green')
main_hobby_label.grid(row=0, column = 0)
fav_genre_label = Label(window, width = 15, text = 'Faviorite genre?')
fav_genre_label.grid(row = 0, column = 1)
Age_label = Label(window, width = 15, text = 'Age')
Age_label.grid(row = 0, column = 2)

# Input_textbox

Agebox = Entry(window, width = 15, bg = 'light blue')
Agebox.grid(row = 1, column = 2)

# Create a tkinter string value:
main_hobby = StringVar()

# Main Hobby Dropdown menu

hobby_options = ('Cooking', 'Football', 'Fishing', 'Hunting')
main_hobby.set('Main hobby?')
main_hobby_dropdown = OptionMenu(window, main_hobby, *hobby_options)
main_hobby_dropdown.grid(row = 1, column = 0)

# fav_genre_dropdown menu

fav_genre = StringVar()

fav_genre_options = ('Action', 'Drama', 'Horror', 'Sicence Fiction')
fav_genre.set('Faviorite genre?')
faviorite_dropdown = OptionMenu(window, fav_genre, *fav_genre_options)
faviorite_dropdown.grid(row = 1, column = 1)

# Button

Match_button = Button(window, width = 10, bg = 'green', text = 'Find a match', command = matcher)
Match_button.grid(row = 0, column = 3)

# Output textbox

output_textbox = Text(window, width = 15, height = 1)
output_textbox.grid(row = 2, column = 0)

window.mainloop()
