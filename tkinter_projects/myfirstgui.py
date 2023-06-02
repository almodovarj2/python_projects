from tkinter import *
import random

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def button_got_clicked():
    my_label['text'] = input.get()

def boom_boom():
    my_label['text'] = 'BOOM 💥'

# Label
my_label = Label(text='What\'s up!', font=("Arial", 24, "bold"))
my_label.pack()
my_label.grid(column=0, row=0)

# Button

button = Button(text='Click here', command=button_got_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=20)
input.get()
input.grid(column=3, row=2)

new_button = Button(text='Don\'t click this!', command=boom_boom)
new_button.grid(column=2, row=0)





window.mainloop()
