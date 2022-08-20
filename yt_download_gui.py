from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry('500x300')
window.configure(bg = '#856ff8')
window.resizable(0,0)
window.title("Download")

Label(window, text="YouTube Video Downloader", font="arial 20 bold", bg = '#856ff8').pack()

Label(window, text = "Paste the link here", font = "arial 17 normal", bg = '#856ff8').place(x = 150, y = 80)

link = StringVar()

link_get = Entry(window,width=70, textvariable= link).place(x=40, y=120)

def Downloader():
    
    yt = YouTube(link.get())
    img = "maxresdefault.jpg"
    yt_resolution = yt.streams.get_highest_resolution()
    yt_resolution.download("C:\\Users\\lette\\OneDrive\\Desktop\\yt download")
    Label(window, image= img , font = "arial 15 bold", bg = 'red' ).place(x=190, y=  10)

Button(window, text = "Download", font = 'arial 15 bold', bg = 'red', padx = 1, command = Downloader).place(x=190, y=150)

window.mainloop()