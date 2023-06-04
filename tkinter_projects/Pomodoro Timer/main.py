from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0
def start_timer():
    if reps == 8:
        timer_text['text'] = 'Long Break'
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        timer_text['text'] = 'Focus'
        count_down(WORK_MIN * 60)
    else:
        timer_text['text'] = 'Short Break'
        count_down(SHORT_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec:02}")
    if count >0:
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, "35", 'bold'))
canvas.grid(column=1, row=1)

# labels
timer_text = Label(text='Timer',bg=YELLOW, fg='#228B22', font=(FONT_NAME, 40, 'bold'))
timer_text.grid(column=1, row=0)

check_label = Label(text='✓', bg=YELLOW, fg="#228B22", font=('Arial', 20, "bold"))
check_label.grid(column=1, row=3)

# buttons
start_button = Button(text='Start', highlightbackground=YELLOW, width=2, font=('Arial', 14, 'bold'), command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text='Reset', highlightbackground=YELLOW, width=2, font=('Arial', 14, 'bold'))
reset_button.grid(column=2, row=2)


window.mainloop()
