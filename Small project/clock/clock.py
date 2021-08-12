# clock program

from tkinter import *
from time import *

def update():
    time_str = strftime("%I:%M:%S %p")
    time_label.config(text=time_str)
    day_str = strftime("%A")
    day_label.config(text=day_str)
    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)
    
    window.after(1000, update)

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack(fill="x")

day_label = Label(window, font=("Ink Free", 25), fg="#00FF00", bg="black")
day_label.pack(fill="both", expand=True)

date_label = Label(window, font=("Ink Free", 25), fg="#00FF00", bg="black")
date_label.pack(fill="both", expand=True)

update()

window.mainloop()
