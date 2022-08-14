from tkinter import *
from datetime import datetime

window = Tk()
window.title("Ywu : The Digital Clock")
window.geometry("400x200")
window.resizable(1,1)
window.config(bg = "#008B8B")

view = Label(window, font="arial 70 bold", bg="#008B8B" , fg="#7FFF00", bd =25)
view.grid(row=0, column =1)

def time():
    
    current_time = datetime.now()
    current_time = current_time.strftime("%H:%M:%S")
    view.config(text=current_time)
    view.after(200,time)

time()
window.mainloop()