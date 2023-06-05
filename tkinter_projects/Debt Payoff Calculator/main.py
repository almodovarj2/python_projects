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
window.config(padx=100, pady=50, bg=BG_COLOR)

canvas = Canvas(width=300, height=224, bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)

# LABELS
# Balance owed
# Estimated Interest Rate
# Monthly payment or Desired months to payoff

# BUTTONS
# Calculate button
# Start over button that only appears after you click the calculate button the first time


window.mainloop()