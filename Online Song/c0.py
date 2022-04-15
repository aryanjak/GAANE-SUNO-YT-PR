import pywhatkit
from tkinter import *
from tkinter.ttk import *
import os

root = Tk()
root.title("Youtube par GAANE SUNE YHA SE")
root.geometry("500x300")


title = Label(root, text="!!SANGEET PAR AB YT SE!!",
              font=("bold", 15)).place(x=120, y=30)


song_text = StringVar()
song_Entry = Entry(root, textvariable=song_text)
song_Entry.place(x=180, y=90)

def ps():
    song = song_text.get()
    pywhatkit.playonyt(song)

listen_button = Button(root, text="Search!", width=12, command=ps)
listen_button.place(x = 350,y=85)


root.mainloop()
