from tkinter import *
import tkinter as tk
import time

# ---------------------------- UI SETUP ------------------------------- #
# Init window
window = tk.Tk()
# set title
window.title('Disappearing Text')
# set full screen
window.state('zoomed')
# set padding
window.config(pady=40, bg='#f6f7f1')

# add text entry
text = tk.Text(width=150, height=45, bg='#f6f7f1', borderwidth=0, fg='#b90000')
text.config(font=('Helvetica', 14))
text.focus_set()
text.pack()


window.mainloop()