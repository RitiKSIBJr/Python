from tkinter import *

window = Tk()
window.geometry('370x400')
window.title("PyCalculaor")
window.config(bg="black")
window.resizable(0,0)

screen = Entry(window, width = 40,  borderwidth = 9, relief = RIDGE)
screen.grid(pady=10, ipady = 10,  row =0 , sticky='w', padx=10)

def delete():
    a = screen.get()
    screen.delete(first=len(a)-1, last = "end")

def result():
    if screen.get()[0] == "0":
        screen.delete(0,"end")
    else:
        c_res = screen.get()
        c_res = eval(c_res)
        clear()
        screen.insert("end",c_res)

def clear():
    screen.delete(0,"end")

clean=Button(window,text="c",width=7,font="arial 13 bold", command=clear,bg="red",fg="white",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=280,ipady=10)

nine = Button(window,text="9",width=7,font="arial 13 bold",command=lambda:screen.insert("end","9"),borderwidth=5, relief=RIDGE)
nine.grid(row=1,sticky="w",padx=15,ipady=10)

eight = Button(window,text="8",width=7,font="arial 13 bold",command=lambda:screen.insert("end","8"),borderwidth=5, relief=RIDGE)
eight.grid(row=1,sticky="w",padx=100,ipady=10)

seven = Button(window,text="7",width=7,font="arial 13 bold",command=lambda:screen.insert("end","7"),borderwidth=5, relief=RIDGE)
seven.grid(row=1,sticky="w",padx=185,ipady=10)

plus = Button(window,text="+",width=7,font="arial 13 bold",command =lambda:screen.insert("end","+"),borderwidth=5,relief=RIDGE)
plus.grid(row=1,sticky="w",padx=280,ipady=10)

six = Button(window,text="6",width=7,font="arial 13 bold",command=lambda:screen.insert("end","6"),borderwidth=5, relief=RIDGE)
six.grid(row=2,sticky="w",padx=15,ipady=10)

five = Button(window,text="5",width=7,font="arial 13 bold",command=lambda:screen.insert("end","5"),borderwidth=5, relief=RIDGE)
five.grid(row=2,sticky="w",padx=100,ipady=10)

four = Button(window,text="4",width=7,font="arial 13 bold",command=lambda:screen.insert("end","4"),borderwidth=5, relief=RIDGE)
four.grid(row=2,sticky="w",padx=185,ipady=10)

minus = Button(window,text="-",width=7,font="arial 13 bold",command=lambda:screen.insert("end","-"),borderwidth=5, relief=RIDGE)
minus.grid(row=2,sticky="w",padx=280,ipady=10)

three = Button(window,text="3",width=7,font="arial 13 bold",command=lambda:screen.insert("end","3"),borderwidth=5, relief=RIDGE)
three.grid(row=3,sticky="w",padx=15,ipady=10)

two = Button(window,text="2",width=7,font="arial 13 bold",command=lambda:screen.insert("end","2"),borderwidth=5, relief=RIDGE)
two.grid(row=3,sticky="w",padx=100,ipady=10)

one = Button(window,text="1",width=7,font="arial 13 bold",command=lambda:screen.insert("end","1"),borderwidth=5, relief=RIDGE)
one.grid(row=3,sticky="w",padx=185,ipady=10)

divide = Button(window,text="/",width=7,font="arial 13 bold",command=lambda:screen.insert("end","/"),borderwidth=5, relief=RIDGE)
divide.grid(row=3,sticky="w",padx=280,ipady=10)

zero = Button(window,text="0",width=7,font="arial 13 bold",command=lambda:screen.insert("end","0"),borderwidth=5, relief=RIDGE)
zero.grid(row=4,sticky="w",padx=15,ipady=10)

double_zero = Button(window,text="00",width=7,font="arial 13 bold",command=lambda:screen.insert("end","00"),borderwidth=5, relief=RIDGE)
double_zero.grid(row=4,sticky="w",padx=100,ipady=10)

dot = Button(window,text=".",width=7,font="arial 13 bold",command=lambda:screen.insert("end","."),borderwidth=5, relief=RIDGE)
dot.grid(row=4,sticky="w",padx=185,ipady=10)

multiply = Button(window,text="*",width=7,font="arial 13 bold",command=lambda:screen.insert("end","*"),borderwidth=5, relief=RIDGE)
multiply.grid(row=4,sticky="w",padx=280,ipady=10)

equal = Button(window,text="=",width=7,font="arial 13 bold",command=result,bg = "red",borderwidth=5, relief=RIDGE)
equal.grid(row=5,sticky="w",padx=15,ipady=10,ipadx=42)

dele = Button(window,text="del",width=7,font="arial 13 bold",command=lambda:screen.insert("end","del"),borderwidth=5, relief=RIDGE)
dele.grid(row=5,sticky="w",padx=185,ipady=10)

modulus = Button(window,text="%",width=7,font="arial 13 bold",command=lambda:screen.insert("end","%"),borderwidth=5, relief=RIDGE)
modulus.grid(row=5,sticky="w",padx=280,ipady=10)




window.mainloop()


