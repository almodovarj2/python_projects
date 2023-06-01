from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text='What\'s up!', font=("Arial", 24, "bold"))
my_label.pack()

# Button

button = Button(text='Click here')
button.pack()  # Elements need to have pack to show up on screen

window.mainloop()
