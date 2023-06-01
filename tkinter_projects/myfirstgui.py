from tkinter import *
import random

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text='What\'s up!', font=("Arial", 24, "bold"))
my_label.pack()


# Button


# def button_got_clicked():
#     button_options = ['Hello World!', 'You\'re cool!', 'I love sushi!', 'Pikmin are cool!']
#
#     my_label['text'] = random.choice(button_options)
def button_got_clicked():
    my_label['text'] = input.get()


button = Button(text='Click here', command=button_got_clicked)
button.pack()  # Elements need to have pack to show up on screen

# Entry
input = Entry(width=20)
input.pack()
input.get()

window.mainloop()
