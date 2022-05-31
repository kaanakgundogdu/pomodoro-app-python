import tkinter
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
reps = 0
timer = None
is_timer_works = False
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps, is_timer_works
    reps = 0
    is_timer_works = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, is_timer_works
    if is_timer_works:
        return

    minute = 60
    reps += 1
    is_timer_works = True

    work_sec = WORK_MIN * minute
    short_break_sec = SHORT_BREAK_MIN * minute
    long_break_sec = LONG_BREAK_MIN * minute

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, is_timer_works
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        is_timer_works = False
        start_timer()
        marks = ""
        for i in range(math.floor(reps / 2)):
            marks += "✓"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="pomodoro/imgs-and-scs/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

canvas.grid(column=1, row=1)

# Label
title_label = tkinter.Label(text="TIMER", font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)


# Button
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(font=("Arial", 12, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
