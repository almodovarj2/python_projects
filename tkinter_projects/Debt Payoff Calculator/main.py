from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = 'Helvetica'
BG_COLOR = '#E5F9DB'


# ---------------------------- CALCULATE DEBT PAYOFF ------------------------------- #

# ---------------------------- CALCULATE DEBT FREE DATE ------------------------------- #

# ---------------------------- CALCULATE INTEREST PAID ------------------------------- #

# ---------------------------- CALCULATE INTEREST PAID ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Debt Payoff Calculator")
window.config(padx=100, pady=10, bg=BG_COLOR)

canvas = Canvas(width=300, height=500, bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)

# LABELS
title_text = Label(text= 'Debt Repayment Calculator', fg='#83764F', bg= BG_COLOR, font=(FONT_NAME, 30, 'bold'))
title_text.grid(row=0, column=1)
# Balance owed
balance_text = Label(text='Balance Owed', fg='black', bg=BG_COLOR, font=(FONT_NAME, 20))
balance_input = Entry(width=10)
balance_text.grid(row=1, column=1)
balance_input.grid(row=2, column=1)
# Estimated Interest Rate
interest_text = Label(text='Estimated Interest', fg='black', bg=BG_COLOR, font=(FONT_NAME, 20))
interest_input = Entry(width=10)
interest_text.grid(row=3, column=1)
interest_input.grid(row=4, column=1)
# Monthly payment or Desired months to payoff

# BUTTONS
# Calculate button
# Start over button that only appears after you click the calculate button the first time


window.mainloop()