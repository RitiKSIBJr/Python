from tkinter import *
import random

window = Tk()
window.geometry('700x400')
window.configure(bg = '#856ff8')
window.resizable(0,0)
window.title("R I T I K")


Label(window, text = "Rock Paper Scissors", font = "arial 25 bold", bg = '#856ff8').pack()
Label(window, text = "Choose r for rock, p for paper and s for scissors", font = "arial 15 normal", bg = '#856ff8').place(x=120,y=100)

choice = StringVar()
get_choice = Entry(window, width = 100, textvariable = choice).place(x = 50, y=150)

def review():
    computer = random.choice(['r','s','p'])

    user = choice.get()

    if user not in ['r','p','s']:
        Label(window,text = "Invalid Character",font ='arial 20 bold', bg= 'red').place(x=300,y=300)    

    elif user == computer:
        Label(window, text = "It's a tie", font = "arial 20 bold" , bg = 'red').place(x=300, y=300)

    else:
        if (user == 's' and computer == 'p') or (user == 'r' and computer == 's') or\
        (user == 'p' and computer == 'r') :
            Label(window, text = "You won", font = "arial 20 bold", bg = "red").place(x=300,y=300)
        
        else:
            Label(window, text = "You Loose", font = "arial 20 bold", bg = "red").place(x=300,y=300)

Button(window, text= "Play", font = "arial 20 bold", bg = "red", padx = 1, command = review).place(x=300, y=200)


window.mainloop()