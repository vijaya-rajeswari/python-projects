import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="#305065")

e = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = g_c.get()
    speed = s_c.get()
    voice = e.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            e.setProperty('voice', voice[0].id)
            e.say(text)
            e.runAndWait()
        else:
            e.setProperty('voice', voice[1].id)
            e.say(text)
            e.runAndWait()

    if text:
        if speed == 'Fast':
            e.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            e.setProperty('rate', 150)
            setvoice()
        else:
            e.setProperty('rate', 60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = g_c.get()
    speed = s_c.get()
    voice = e.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            e.setProperty('voice', voice[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            e.save_to_file(text,"text.mp3")
            e.runAndWait()
        else:
            e.setProperty('voice', voice[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            e.save_to_file(text, "text.mp3")
            e.runAndWait()

    if text:
        if speed == 'Fast':
            e.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            e.setProperty('rate', 150)
            setvoice()
        else:
            e.setProperty('rate', 60)
            setvoice()


# icon
icon_image = PhotoImage(file="my.png")
root.iconphoto(False, icon_image)

# top frame
t = Frame(root, bg="white", width=900, height=100)
t.place(x=0, y=0)

Label(t, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

# Text area
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

g_c = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
g_c.place(x=550, y=200)
g_c.set('Male')

s_c = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
s_c.place(x=730, y=200)
s_c.set('Normal')

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

# Speak button
b = Button(root, text="Speak", compound=LEFT, width=10, font="arial 14 bold", command=speaknow)
b.place(x=550, y=280)

# Save button
b = Button(root, text="Save", compound=LEFT, width=10, bg="#39c790", font="arial 14 bold", command=download)
b.place(x=730, y=280)

root.mainloop()
