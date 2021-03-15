import math


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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_test 00:00
    canvas.itemconfig(timer_text,text="00:00")
    # title_label "Timer"
    title_label.config(text="Timer")
    # reset check marks
    tick_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def starting_button():
    global reps
    work_sec = WORK_MIN * 60
    work_break = SHORT_BREAK_MIN * 60
    work_break_long = LONG_BREAK_MIN * 60

    reps+=1

    if reps % 8 == 0:
        count_down(work_break_long)
        title_label.config(text=" Long Break", fg=RED, font=(FONT_NAME,50))
    elif reps % 2 == 0:
        count_down(work_break)
        title_label.config(text=" Short Break", fg=PINK, font=(FONT_NAME,50))
    else:
        count_down(work_sec)
        title_label.config(text=" work Time", fg=RED, font=(FONT_NAME,50))

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = (count% 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        starting_button()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"

        tick_label.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
# setting the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# Label (Timer)
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=1,row=0)

tick_label = Label(fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=3)


# uploading img to canvas

canvas = Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


# Button

start_button = Button(text="Start",highlightthickness=0,command=starting_button)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)



window.mainloop()