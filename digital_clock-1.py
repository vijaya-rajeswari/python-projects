from tkinter import Tk
from tkinter import Label
import time
import sys
# import PhotoImage
m = Tk()
m.title("Digital Clock")

# icon_image= PhotoImage(file="digital-clock.jpg")
# root.iconphoto(False,icon_image)

def get_time():
    t = time.strftime("%H:%M:%S")
    clock.config(text=t)
    clock.after(200,get_time)

Label(m,font=("arial",30),text="Digital Clock",bg="pink",fg="black").pack()
clock = Label(m,font=("arial",100),bg="pink",fg="black")
clock.pack()

get_time()
m.mainloop()


