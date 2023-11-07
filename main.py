from tkinter import *
import tkinter as tk
import time

# Desktop app
# Don't stop typing otherwise the text will disappear after 5 sec

# number of letters that user has written so far
characters = 0

# time to disappear
time_to_d = 5

# next color
n_color = 0

def check(timer):
    """check if user stopped typing"""
    global characters, time_to_d, n_color

    # colors to animate a fade away effect
    colors = ['#ff0000', '#ff2424', '#ff4747', '#ff6b6b', '#ff8f8f', '#ffb3b3', '#f6f7f1']

    # length of text entry
    text_len = len(text.get("1.0", END))
    # check if user stopped typing
    if text_len == characters:
        # display sec left to disappear
        timer_label.config(text=time_to_d)
        # change text color
        text.config(fg=colors[n_color])
        # minus 1 sec
        n_color += 1
        # next color
        time_to_d -= 1
    else:
        # reset color
        n_color = 0
        # reset timer
        time_to_d = 5
        # hide timer
        timer_label.config(text="")
        # reset color
        text.config(fg='#ff0000')
        characters = text_len
    # timer equal 0 -> delete text
    if time_to_d == -2:
        # reset color
        n_color = 0
        # reset timer
        time_to_d = 5
        timer_label.config(text="")
        text.config(fg='#ff0000')
        with open('your_last_text.txt', 'w') as file:
            file.write(text.get("1.0", END))
        text.delete('1.0', END)

    # check every second if user stopped typing
    window.after(1000, check, time_to_d)


# ---------------------------- UI SETUP ------------------------------- #


# Init window
window = tk.Tk()
# set title
window.title('Disappearing Text')
# set full screen
window.state('zoomed')
# set padding
window.config(pady=40, bg='#f6f7f1')
# add timer label
timer_label = tk.Label()
timer_label.config(text='',
                   fg='#ff0000',
                   font=('Helvetica', 20),
                   bg='#f6f7f1',
                   pady=20)
timer_label.pack()

# add text entry
text = tk.Text(width=150,
               height=40,
               bg='#f6f7f1',
               borderwidth=0,
               fg='#ff0000',
               padx=20)
text.config(font=('Helvetica', 14))
# set cursor focus
text.focus_set()
text.pack()

check(time_to_d)

window.mainloop()
