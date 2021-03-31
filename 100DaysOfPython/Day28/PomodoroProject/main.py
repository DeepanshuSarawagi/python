from tkinter import *

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1, pady=20)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
timer_label.grid(row=0, column=1)


start_button = Button(text="Start", bg=YELLOW, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2)

tick_label = Label(text="✅", bg=YELLOW)
tick_label.grid(row=2, column=1)

window.mainloop()
