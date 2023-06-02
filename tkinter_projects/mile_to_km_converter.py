from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=80, pady=50)


# Function to convert input
def miles_to_km():
    miles = input.get()
    kms = round((float(miles) * 1.609), 1)
    converted_output['text'] = kms


# One input
input = Entry(width=10)
input.grid(column=1, row=0)

# Four labels
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

km = Label(text='Km')
km.grid(column=2, row=1)

converted_output = Label(text=0)
converted_output.grid(column=1, row=1)

# One button
calculate = Button(text='Calculate', command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
