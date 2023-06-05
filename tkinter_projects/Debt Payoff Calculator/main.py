from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = 'Helvetica'
BG_COLOR = '#E5F9DB'


# ---------------------------- CALCULATE DEBT PAYOFF ------------------------------- #

# ---------------------------- CALCULATE DEBT FREE DATE ------------------------------- #

# ---------------------------- CALCULATE INTEREST PAID ------------------------------- #

# ---------------------------- CALCULATE MONTHS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Debt Payoff Calculator")
window.minsize(width=300, height=500)
window.config(padx=100, pady=10, bg=BG_COLOR)

# LABELS
title_text = Label(text= 'Debt Repayment Calculator', fg='#83764F', bg= BG_COLOR, font=(FONT_NAME, 30, 'bold'))
title_text.grid(row=0, column=1)
# Balance owed
balance_text = Label(text='Balance Owed', fg='black', bg=BG_COLOR, font=(FONT_NAME, 20))
balance_input = Entry(width=10, bg='white', fg='black', highlightthickness=1)
balance_text.grid(row=1, column=1,pady=(20, 0))
balance_input.grid(row=2, column=1)

# Estimated Interest Rate
interest_text = Label(text='Estimated Interest', fg='black', bg=BG_COLOR, font=(FONT_NAME, 20))
interest_input = Entry(width=10, bg='white', fg='black',highlightthickness=1)
interest_text.grid(row=3, column=1, pady=(20, 0))
interest_input.grid(row=4, column=1)
# Monthly payment or Desired months to payoff

# BUTTONS
# Calculate button
calculate_button = Button(text='Calculate', bg=BG_COLOR, highlightbackground=BG_COLOR, font=(FONT_NAME, 20, 'bold'))
calculate_button.grid(row=5, column=1, padx=(0, 150), pady=(20, 0))
# Start over button that only appears after you click the calculate button the first time
start_over = Button(text='Start Over', bg=BG_COLOR, highlightbackground=BG_COLOR, font=(FONT_NAME, 20, 'bold'))
start_over.grid(row=5, column=1, padx=(150, 0), pady=(20, 0))
window.mainloop()